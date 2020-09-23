import unittest

from src.py.UnwantedDataFilter import filterDicts


class TestUnwantedDataFiler(unittest.TestCase):
    def test_shouldReturn_A_B_keys_given_1_key_is_not_matched(self):
        dictOne = {'a': 2, 'b': 3, 'c': 6}
        dictTwo = {'a': 3, 'b': 5, 'd': 2}
        self.assertEqual(filterDicts(dictOne, dictTwo), {'a': 2, 'b': 3})

    def test_shouldReturn_A_B_C_keys_given_all_keys_are_matched(self):
        dictOne = {'a': 3, 'b': 5, 'c': 2}
        dictTwo = {'a': 2, 'b': 3, 'c': 6}
        self.assertEqual(filterDicts(dictOne, dictTwo), {'a': 3, 'b': 5, 'c': 2})

    def test_shouldReturn_No_keys_given_no_match_dicts(self):
        dictOne = {'a' : 3, 'b': 5, 'c': 2}
        dictTwo = {}
        self.assertEqual(filterDicts(dictOne, dictTwo), {})