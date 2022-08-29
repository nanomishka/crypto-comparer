import os
import aiohttp
import aiofiles

import pandas as pd

import settings


def _filename_from_url(url):
    return url.split("/")[-1]


async def fetch_dataframes(datasets):
    if not os.path.exists(settings.DATA_DIR):
        os.makedirs(settings.DATA_DIR)

    dataframes = {}

    for name, url in datasets.items():

        filename = _filename_from_url(url)
        filepath = f'{settings.DATA_DIR}/{filename}'

        if not os.path.isfile(filepath):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:

                        f = await aiofiles.open(filepath, mode='wb+')
                        await f.write(await resp.read())
                        await f.close()

        dataframes[name] = pd.read_csv(filepath)

    return dataframes
