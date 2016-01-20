#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.library_name }}
----------------------------------

Tests for `{{ cookiecutter.library_name }}` module.
"""

import unittest

from {{ cookiecutter.library_name }} import {{ cookiecutter.library_name }}


class Test{{ cookiecutter.library_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
