#!/usr/bin/python3
"""implements zoom_array
"""
from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[Any]:
    """takes a list and a factor that returns a list
    of a number of values as specified by factor
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
