#!/usr/bin/env python3

import sys

class Book(object):
    def __init__(self, title, page_count):
        self.title = title
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            sys.stdout.write(u"page_count must be an integer\n")
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            sys.stdout.write(u"page_count must be an integer\n")
    
    def turn_page(self):
        sys.stdout.write(u"Flipping the page...wow, you read fast!\n")