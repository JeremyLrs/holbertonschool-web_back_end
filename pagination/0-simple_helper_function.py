#!usr/bin/env python3
"""
Fonction to help for pagination
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and the end of pagination
    """

    page_init = (page - 1) * page_size
    end_page = page_init + page_size

    return (page_init, end_page)
