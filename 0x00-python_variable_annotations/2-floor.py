#!/usr/bin/python3
"""implements floor
"""


def floor(n: float) -> int:
    """takes a float n as argument
    and returns the floor of the float.
    """
    if n >= 0:
        return int(n)
    else:
        int_part = int(n)
        return int(n) if int_part == n else int_part - 1
