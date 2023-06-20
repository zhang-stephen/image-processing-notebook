#!/bin/python3

from imgtools.ImageHosting import smms_app
from imgtools.utils import ASSETS_DIR

import pandas as pds
from pathlib import Path
from typing import Union

IMG_HOSTING = {'smms': smms_app}


def imgs_fetch(img_list_csv: Union[str, Path]):
    img_list_csv = img_list_csv if isinstance(img_list_csv, Path) else Path(img_list_csv)

    if not img_list_csv.exists():
        raise FileNotFoundError(f'Cannot found valid imagelist: {img_list_csv}')

    img_list = pds.read_csv(img_list_csv, index_col=False)

    for _, (hashes, filename, hosting) in img_list.iterrows():
        print(f'fetching {hashes} as {filename} from {hosting}...')
        IMG_HOSTING[hosting](hashes, ASSETS_DIR / filename)


if __name__ == '__main__':
    ASSETS_DIR.mkdir(mode=0o755, parents=True, exist_ok=True)
    imgs_fetch('./imglist.csv')
