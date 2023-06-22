#!/bin/python3

import math as m


def find_ceil_pow2(num: int) -> int:
    if num < 0:
        raise ValueError(r'num should not be less than 0')

    return 1 if num == 0 else 2 ** (int(m.log2(num)) + 1)


# EOF
