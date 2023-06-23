#!/bin/python3

import math as m


def find_ceil_pow2(num: int, *, exp: int = 8) -> int:
    if num < 0:
        raise ValueError(r'num should not be less than 0')

    return max(2**exp, 1 if num == 0 else 2 ** (int(m.log2(num)) + 1))


# EOF
