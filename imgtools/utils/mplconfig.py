#!/bin/python3

from matplotlib import pyplot as plt


def mpl_config():
    rc_params = {'figure.figsize': (12.0, 6.0)}

    for k, v in rc_params.items():
        plt.rcParams[k] = v


# EOF
