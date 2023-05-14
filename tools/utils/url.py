#!/bin/python3

from __future__ import annotations


class UniformResourceLocator:
    def __init__(self, s: str):
        self.url = s
        self.is_end_with_slash = s.endswith('/')

    def __truediv__(self, other: str) -> UniformResourceLocator:
        if self.is_end_with_slash:
            return UniformResourceLocator(self.url + other)
        else:
            return UniformResourceLocator(f'{self.url}/{other}')

    def __str__(self) -> str:
        return self.url

    def __call__(self) -> str:
        return str(self)

    def __repr__(self) -> str:
        return str(self)


# EOF
