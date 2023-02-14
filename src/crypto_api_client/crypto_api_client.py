import datetime
import json
import os

import requests


BASE_URL = "https://rest.coinapi.io"
API_KEY = os.environ.get("COINAPI_API_KEY")


def main():
    start = datetime.datetime(year=2022, month=1, day=1, hour=0)
    end = datetime.datetime(year=2023, month=1, day=1, hour=0)
    data = get_history(start, end)

    with open("./data/data.json", "w") as f:
        json.dump(data, f)


def get_history(start: datetime.datetime, end: datetime.datetime) -> requests.Request:
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
