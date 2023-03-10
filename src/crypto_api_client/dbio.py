from dataclasses import dataclass
import datetime
import json
import os
import sqlite3


@dataclass
class CoinAPIRow:
    """Represents a returned row from CoinAPI.

    Example:
        {
          "time_period_start": "2022-11-07T00:00:00.0000000Z",
          "time_period_end": "2022-11-08T00:00:00.0000000Z",
          "time_open": "2022-11-07T00:00:00.0000000Z",
          "time_close": "2022-11-07T23:59:00.0000000Z",
          "rate_open": 20908.745035238324,
          "rate_high": 21061.986585685365,
          "rate_low": 20400.280815874907,
          "rate_close": 20591.055715405393
        }
    """

    rate_close: float
    rate_high: float
    rate_low: float
    rate_open: float
    time_close: str
    time_open: str
    time_period_end: str
    time_period_start: str


@dataclass
class SQLiteRow:
    """Reprsents a row in our destination database.

    "Spread" means rate_high minus rate_low.
    """

    date: datetime.date
    year: int
    month: str
    weekday: str
    calweek: int
    spread: int


def main():
    """Saves data to a database for low latency queries.

    Once the data is downloaded with the "crypto_api_client", this function
    will save its output to a database.

    Each file from data represents 100 rows of coinapi.
    """
    conn = sqlite3.connect("data/sqlite3/data.db")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS btc_usd_spread;")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS btc_usd_spread (
            date TEXT PRIMARY KEY,
            year INTEGER,
            month INTEGER,
            weekday TEXT,
            calweek INTEGER,
            spread INTEGER
        )
        """
    )
    conn.commit()

    for file in os.listdir("data"):
        if not file.endswith(".json"):
            continue
        print("Processing file data/" + file)
        f = open("data/" + file, "r")
        data = json.load(f)
        f.close()

        sqlite_rows = []
        for row in data:
            try:
                src_row = CoinAPIRow(
                    rate_close=row["rate_close"],
                    rate_high=row["rate_high"],
                    rate_low=row["rate_low"],
                    rate_open=row["rate_open"],
                    time_close=row["time_close"],
                    time_open=row["time_open"],
                    time_period_end=row["time_period_end"],
                    time_period_start=row["time_period_start"],
                )

            except KeyError:
                raise KeyError("Required field was not in src data.")

            date_str = src_row.time_open.split("T")[0]
            date = datetime.date.fromisoformat(date_str)
            if date.month == 5 and date.year == 2020:
                print(src_row)
            dst_row = SQLiteRow(
                date=date,
                year=date.year,
                month=date.strftime("%b"),
                weekday=date.strftime("%a"),
                calweek=parse_calweek(date),
                spread=int(src_row.rate_high - src_row.rate_low),
            )
            row_as_tuple = (
                dst_row.date,
                dst_row.year,
                dst_row.month,
                dst_row.weekday,
                dst_row.calweek,
                dst_row.spread,
            )
            sqlite_rows.append(row_as_tuple)

        cur.executemany(
            "INSERT INTO btc_usd_spread VALUES (?, ?, ?, ?, ?, ?)", sqlite_rows
        )
        conn.commit()
        print(f"Inserted {len(sqlite_rows)} records into db.")


def parse_calweek(date: datetime.date) -> int:
    """To visualise correctly, we want to have 53 cal weeks in a year."""
    calweek = date.isocalendar()[1]
    if calweek == 52 and date.month == 1:
        return 0
    elif calweek == 1 and date.month > 1:
        return 53
    else:
        return calweek


if __name__ == "__main__":
    main()
