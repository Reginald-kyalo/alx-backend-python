#!/usr/bin/python3
"""implements make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument
    and returns a function
    that multiplies a float by multiplier
    """
    def float_sum(x: float) -> float:
        return multiplier * x
    return float_sum
