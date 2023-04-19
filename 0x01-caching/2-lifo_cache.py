#!/usr/bin/env python3
'''LIFO caching system'''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''Implements a LIFO caching system'''

    def __init__(self):
        '''Initializes the cache'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Puts an item and removes the last item if cache is full'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            poppedKey, item = self.cache_data.popitem(True)
            print('DISCARD: {}'.format(poppedKey))

    def get(self, key):
        '''Gets the item tied to key in cache'''
        return self.cache_data.get(key)
