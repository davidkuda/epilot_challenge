import datetime
import json
import os

import requests


BASE_URL = "https://rest.coinapi.io"
API_KEY = os.environ.get("COINAPI_API_KEY")


def main():
    """This app requests coinapi and gets the historical data of the
    exchange rates of bitcoin in USD.

    The coinapi returns only 100 results, and it offers no pagination.
    Therefore, this code implements an algorithm based on datetime calculation
    to retrieve multiple slices of 100 days.
    """
    end = datetime.date.today()
    start = end - datetime.timedelta(days=100)

    count = 1

    while start > datetime.date(year=2010, month=1, day=1):
        print(f"{count}: Getting data from {start} to {end}")
        data = get_history(start, end)

        with open(f"./data/{start}--{end}.json", "w") as f:
            json.dump(data, f)

        end = start
        start = end - datetime.timedelta(days=100)
        count += 1


def get_history(start: datetime.date, end: datetime.date) -> requests.Request:
    return requests.get(
        BASE_URL + "/v1/exchangerate/BTC/USD/history",
        params={
            "period_id": "1DAY",
            "time_start": start.isoformat(),
            "time_end": end.isoformat(),
        },
        headers={"X-CoinAPI-Key": "FC546E7C-76CF-4D89-9B01-69C5D64421E9"},
    ).json()


if __name__ == "__main__":
    main()
