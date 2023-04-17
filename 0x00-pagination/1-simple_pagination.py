#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple
'''Pagination File that returns from a set of data'''


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Function that takes two args and returns pagination params'''
    first = (page - 1) * page_size
    last = first + page_size
    return (first, last)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns data after pagination'''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        first, last = index_range(page, page_size)
        data = self.dataset()
        if first > len(data):
            return []
        return data[first:last]
