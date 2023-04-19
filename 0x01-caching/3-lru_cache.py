#!/usr/bin/env python3
'''LRU caching system'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''Implements a LRU caching system'''

    def __init__(self):
        '''Initializes the cache'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Puts an item and removes the last item if cache is full'''
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                poppedKey, itemPopped = self.cache_data.popitem(True)
                print('DISCARD: {}'.format(poppedKey))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, False)

    def get(self, key):
        '''Gets the item tied to key in cache and moves it to top'''
        if key in self.cache_data:
            self.cache_data.move_to_end(key, False)
            return self.cache_data.get(key)
