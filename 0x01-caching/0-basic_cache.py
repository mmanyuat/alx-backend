#!/usr/bin/env python
"""BasicCache Module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching and is a caching system
    - This cache has no limit on number of items.
    """
    def put(self, key, item):
        """checks if the key and value is present
        and adds it to the dict
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns the dict if the key exists"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
