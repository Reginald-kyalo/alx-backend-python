#!/usr/bin/env python3
"""implements safe_first_element
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """takes a list and returns the first value of the list
    or None if list is not available
    """
    if lst:
        return lst[0]
    else:
        return None
