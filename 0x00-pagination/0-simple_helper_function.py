#!/usr/bin/env python3
'''A simple helper function'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Function that takes two args and returns pagination params'''
    first = (page - 1) * page_size
    last = first + page_size
    return (first, last)
