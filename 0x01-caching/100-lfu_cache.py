#!/usr/bin/env python3
"""LFU algorithm"""

from base_caching import BaseCaching
"""base class"""


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """Assigns the item to te and applies LFU policy if necessary."""
        if key is None or item is None:
            return

        # Update cache and frequency/order tracking
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Determine the LFU (and LRU if needed) key to discard
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k, freq in self.usage_frequency.items()
                            if freq == min_freq]
                if len(lfu_keys) > 1:
                    # Choose the LRU among the LFU keys
                    lfu_key = next(k for k in self.usage_order
                                   if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                # Discard the chosen key
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Insert the new key with initial frequency of 1
            self.cache_data[key] = item
            self.usage_frequency[key] = 1

        # Update the usage order to reflect most recent usage
        self.usage_order.append(key)

    def get(self, key):
        """Gets the item associated with the key, updating its usage status."""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and usage order for LFU
        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
