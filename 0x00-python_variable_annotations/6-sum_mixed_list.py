#!/usr/bin/env python3
"""
This module contains a type annotated python function
"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float
    """
    return sum(mxd_list)
