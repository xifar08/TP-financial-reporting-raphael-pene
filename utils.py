"""Utility functions or financial reporting"""

import pandas as pd


def get_data(url: str) -> pd.DataFrame:
    return pd.read_parquet(url)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(
        score=df["score"].fillna("S"),
        score_prev=df["score_prev"].fillna("N"),
        id_agent=df["id_agent"].where(df["id_agent"] == "AUTO", "MANUEL"),
    )
    return df


def generate_excel(df: pd.DataFrame, path_file: str):
    with pd.ExcelWriter(
        path_file, mode="a", engine="openpyxl", if_sheet_exists="replace"
    ) as writer:
        df.to_excel(writer, sheet_name="DATA", index=False)
