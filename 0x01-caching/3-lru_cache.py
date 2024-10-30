#!/usr/bin/env python3
"""LRU Caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class that uses the LRU (Least Recently Used) algorithm."""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.usage_order = []  # List to track access order for LRU

    def put(self, key, item):
        """Logic of LRU-algorithm"""
        if key is None or item is None:
            return

        # Remove the key if it already exists to update its position
        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        # Check if cache exceeds maximum size
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict the least recently used item (first in usage_order)
            oldest_key = self.usage_order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve value for the given key"""
        if key is None or key not in self.cache_data:
            return None

        # Update access order by moving the accessed key to the end
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
