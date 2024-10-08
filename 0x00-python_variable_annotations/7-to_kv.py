#!/usr/bin/env python3
"""implements to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """takes a string k and an int OR float v as arguments
    and returns a tuple"""
    return tuple(k, v)
