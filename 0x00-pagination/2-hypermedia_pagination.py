#!/usr/bin/env python3
"""Importing a bunch of modules to support the file """
import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """
    A function that takes two integers parameters
    page: normally the sarting
    page_size: where the page ends
    """
    startIndex = (page - 1) * page_size
    endIndex = (page * page_size)
    return (startIndex, endIndex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of requested baby names for the file"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        dataset = self.dataset
        if startIndex >= len(dataset):
            return []
        return dataset[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary with metadata for the request"""
        data = self.get_page(page, page_size)
        page_size_actual = len(data)
        total_pages = math.ceil(len(self.dataset) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
                "page_size": page_size_actual,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages,
                }
