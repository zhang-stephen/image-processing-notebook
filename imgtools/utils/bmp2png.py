#!/bin/python3

import sys
from pathlib import Path
from typing import Union

from PIL import Image


def bmp2png(src: Union[str, Path]):
    src = src if isinstance(src, Path) else Path(src)
    dst = src.with_suffix('.png')

    with Image.open(src) as bmp:
        if bmp.format != 'BMP':
            return

        bmp.save(dst)


if __name__ == '__main__':
    bmp2png(sys.argv[1])
