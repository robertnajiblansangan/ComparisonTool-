from unittest import TestCase
from unittest.mock import patch, Mock
from src.py.CompareItV2 import compareIt


class Test(TestCase):
    @patch("pandas.DataFrame.to_csv")
    def test_should_call_to_csv_method_given_discrepancy_files(self, to_csv):
        testDataPath1 = 'testData/PSA'
        testDataPath2 = 'testData/PSA2'
        compareIt(testDataPath1, testDataPath2)
        to_csv.assert_called()

