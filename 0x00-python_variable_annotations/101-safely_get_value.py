#!/usr/bin/python3
"""implements safely_get_value
"""
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """takes a dictionary, key of dictionary, default (None) value
    and returns either the value pointed by the key or default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
