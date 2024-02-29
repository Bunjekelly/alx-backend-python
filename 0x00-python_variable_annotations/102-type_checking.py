#!/usr/bin/env python3
"""
This module contains the corrected version of the zoom_array function
"""
from typing import Any
from typing import List
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return a list of integers repeating a given number of times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
