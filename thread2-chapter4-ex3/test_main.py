import unittest

from main import catch_thief

class TestMain(unittest.TestCase):
    def test_queue_1(self):
        self.assertEqual(catch_thief("X1X#2X#XX"), 3)

    def test_queue_2(self):
        self.assertEqual(catch_thief("X5X#3X###XXXX##1#X1X"), 5)

    def test_queue_3(self):
        self.assertEqual(catch_thief("X#X1#X9XX"), 5)

    def test_queue_4(self):
        self.assertEqual(catch_thief("XX1#X1#X9X####X####2XX#X1"), 9)

    def test_queue_5(self):
        self.assertEqual(catch_thief("XX1#X1#X#X####X####2XX#X1"), 5)