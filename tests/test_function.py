import unittest
from function import utils


class TestUtils(unittest.TestCase):

    def test_load(self):
        self.assertEqual(utils.load_data([1, 2, 3], 1, "test"), 3)
        self.assertEqual(utils.load_data([], 0, "test"), "test")


    def test_init(self):
        self.assertEqual(utils.init_operation([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(utils.init_operation([1, 2, 3], 1), [2, 3])
        self.assertEqual(utils.init_operation([], 0,-1), [])
        self.assertEqual(utils.init_operation([1, 2, 3], -1,0), [])
        self.assertEqual(utils.init_operation([1, 2, 3], -4, 0), [])


