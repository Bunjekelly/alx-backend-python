#!/usr/bin/env python3
"""
This module contains a type annotated function element_length
"""
from typing import Iterable
from typing import List
from typing import Sequence
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that takes an iterable and returns a list of tuples of the
    element value and index
    """
    return [(i, len(i)) for i in lst]
