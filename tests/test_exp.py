# -*- coding: utf-8 -*-

import exp

import unittest

class ExpTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(exp.add(1,2), 3)

    def test_min(self):
        self.assertEqual(exp.min(3,2), 1)
