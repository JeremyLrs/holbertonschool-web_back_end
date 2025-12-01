#!usr/bin/env python3
"""
Fonction to help for pagination
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and the end of pagination
    """

    return (page_size * (page - 1), page_size * page)
