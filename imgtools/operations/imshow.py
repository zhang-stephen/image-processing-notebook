#!/bin/python3
from typing import Union

import numpy as np
from matplotlib import pyplot as plt

from .algorithm import find_ceil_pow2


def imshow(
    im: Union[np.ndarray, list[list]], nrows=1, ncols=1, index=1, *, cmap: str = 'gray', title: str = '', width: int = 8
):
    if index > ncols * nrows:
        raise ValueError(f'Invalid subplot index {index} for {nrows} rows and {ncols} columns')

    pixel_ceil = find_ceil_pow2(np.max(im), exp=width)
    plt.subplot(nrows, ncols, index)
    plt.imshow(im, cmap=cmap, vmin=0, vmax=pixel_ceil)

    if len(title) > 0:
        plt.title(title)

    if index == ncols * nrows:
        plt.show()

# EOF
