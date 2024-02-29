#!/usr/bin/env python3
"""
This module contains a type annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier
    """
    def func(number: float) -> float:
        """
        multiplier function that is returned by the make_multiplier function
        """
        return number * multiplier
    return func
