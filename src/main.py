import asyncio

import pandas as pd

from src import constants
from src import settings
from src.download import fetch_dataframes


async def main():
    datasets = settings.DATASETS_URLS
    dataframes = await fetch_dataframes(datasets)

    for df in dataframes.values():
        df.columns = constants.COLUMN_NAMES_MAPPING.values()

    merged_df = pd.merge(
        dataframes["ETHUSDT"],
        dataframes["ETHUSDC"],
        how="inner",
        on="Open_time",
        suffixes=("_ETHUSDT", "_ETHUSDC"),
    )

    merged_df["Open ETHUSDT-ETHUSDC"] = merged_df["Open_ETHUSDT"] - merged_df["Open_ETHUSDC"]

    print(merged_df[['Open_time', 'Open ETHUSDT-ETHUSDC']])

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
