#!/bin/python3

import sys
from pathlib import Path
from typing import Union

from PIL import Image


def any2png(src: Union[str, Path]):
    src = src if isinstance(src, Path) else Path(src)
    dst = src.with_suffix('.png')

    with Image.open(src) as im:
        if im.format not in ['BMP', 'TIFF']:
            return

        im.save(dst)


if __name__ == '__main__':
    any2png(sys.argv[1])
