#!/usr/bin/env python3
'''Implements a fifo caching system'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''Class with a fifo caching method'''

    def __init__(self):
        '''Initializes the class'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Puts an item and if cache is full removes the first item'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            poppedItem = self.cache_data.popitem(False)
            print('DISCARD: {}'.format(poppedItem.keys()))

    def get(self, key):
        '''Returns data associated with key'''
        return self.cache_data.get(key)
