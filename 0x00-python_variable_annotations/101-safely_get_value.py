#!/usr/bin/env python3
"""
This module contains a type annotated function safely_get_value"""
from typing import Any
from typing import Mapping
from typing import TypeVar
from typing import Union
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    This function return the value of key from a dict if present or the default
    keyword argument supplied
    """
    if key in dct:
        return dct[key]
    else:
        return default
