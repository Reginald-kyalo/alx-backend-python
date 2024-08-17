#!/usr/bin/env python3
"""implements element_length
"""
from typing import Iterable, List


def element_length(lst: Iterable[list]) -> List[int]:
    """takes list and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
