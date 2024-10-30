#!/usr/bin/env python3
""" LIFO Caching"""

from base_caching import BaseCaching
"""Gets the base class"""


class LIFOCache(BaseCaching):
    """inheriting from the base_class"""
    def __init__(self):
        """The constructor"""
        super().__init__()

    def put(self, key, item):
        """Assigning Key item to the dict"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item

    def get(self, key):
        """Returns the values in dicts"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
