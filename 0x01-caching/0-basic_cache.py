#!/usr/bin/env python3
'''Basic Python Dictionary'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Class that inherits from BaseCaching'''

    def put(self, key, item):
        '''assign to the dictionary self.cache_data item value for the key'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Returns the value in self.cahce_data corresponding to key'''
        return self.cache_data.get(key)
