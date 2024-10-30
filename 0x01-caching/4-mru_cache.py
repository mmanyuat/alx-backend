#!/usr/bin/env python3
"""MRU algorithmns"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Assigns the item  MRU policy if necessary."""
        if key is None or item is None:
            return

        # Update cache and usage order
        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Insert the new or updated key at the end (most recently used)
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Gets the item associated with the key, updating its usage status."""
        if key is None or key not in self.cache_data:
            return None

        # Update usage order for MRU
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
