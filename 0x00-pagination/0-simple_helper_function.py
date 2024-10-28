#!/usr/bin/env python3
"""Nothing imported"""


def index_range(page: int, page_size: int) -> tuple:
    """
    A function that takes two integers parameters
    page: normally the sarting
    page_size: where the page ends
    """
    startIndex = (page - 1) * page_size
    endIndex = (page * page_size)
    return (startIndex, endIndex)
