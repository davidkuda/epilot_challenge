import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


def main():
    st.write("# Bitcoin USD Spread HeatMap")

    fig, ax = plt.subplots(figsize=(7, 7))

    year = st.selectbox(
        "Choose a year:",
        reversed(range(2010, 2024)),
        index=1,
    )

    visualise_heatmap(year)
    st.write(fig)

    st.write("Developed by David Kuda [www.kuda.ai](https://kuda.ai)")
    st.write("Find the code on [GitHub.com/davidkuda/epilot_challenge](https://github.com/davidkuda/epilot_challenge/blob/main/src/crypto_api_client/visualisation.py)")


def visualise_heatmap(year: int):
    df = read_into_pd_df(year)
    return sns.heatmap(
        df,
        linewidth=0.2,
        square=True,
        cmap="Oranges",
        yticklabels=False,
        xticklabels=False,
        cbar_kws={"shrink": 0.3},
    )


def read_into_pd_df(year: int):
    """Connect to sqlite3 db, read btc usd spread from given year, and reshape df."""
    conn = sqlite3.connect("data/sqlite3/data.db")
    df = pd.read_sql_query(
        f"""
        SELECT calweek, weekday, spread
        FROM btc_usd_spread
        WHERE year = {year}
        ORDER BY date(date)
        ;
        """,
        conn,
    )
    conn.close()
    return reshape(df)


def reshape(df: pd.DataFrame) -> pd.DataFrame:
    r = df.pivot(index="weekday", columns="calweek", values="spread").fillna(0)
    r.columns.name = None
    r.index.name = None
    return r


if __name__ == "__main__":
    main()
