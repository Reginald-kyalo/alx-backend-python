#!/usr/bin/env python3
"""implements sum_mixed_list
"""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """ takes a list mxd_lst of integers and floats
    and returns their sum as a float."""
    sum = 0.0
    for x in mxd_list:
        sum += x
    return sum
