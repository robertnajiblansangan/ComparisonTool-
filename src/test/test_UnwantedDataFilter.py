from unittest import TestCase

from src.py.UnwantedDataFilter import filterDicts


class Test(TestCase):
    def test_UnwantedDataFilter(self):
        with self.subTest('shouldReturn A B keys given 1 key is not matched'):
            dictOne = {'a': 2, 'b': 3, 'c': 6}
            dictTwo = {'a': 3, 'b': 5, 'd': 2}
            self.assertEqual(filterDicts(dictOne, dictTwo), {'a': 2, 'b': 3})

        with self.subTest('shouldReturn_A_B_keys_given_1_key_is_not_matched'):
            dictOne = {'a': 2, 'b': 3, 'c': 6}
            dictTwo = {'a': 3, 'b': 5, 'd': 2}
            self.assertEqual(filterDicts(dictOne, dictTwo), {'a': 2, 'b': 3})

        with self.subTest('shouldReturn_No_keys_given_no_match_dicts'):
            dictOne = {'a': 3, 'b': 5, 'c': 2}
            dictTwo = {}
            self.assertEqual(filterDicts(dictOne, dictTwo), {})
