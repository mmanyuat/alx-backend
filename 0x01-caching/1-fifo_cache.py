#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching
"""Importing the base Class"""


class FIFOCache(BaseCaching):
    """A subclass that inherits from the base"""

    def __init__(self):
        """The constructor"""
        super().__init__()

    def put(self, key, item):
        """Assigning the key, item to the dict"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """return the value key in te dict"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
