#!/usr/bin/python3
"""implements sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    sum = 0.0
    for x in input_list:
        sum += x
    return sum
