from unittest import TestCase
from unittest.mock import patch, Mock
from src.py.CompareItV2 import compareIt


class Test(TestCase):
    def test_should_(read_sql_mock: Mock):
        # testDataPath1 = 'testData/PSA'
        # testDataPath2 = 'testData/PSA2'
        # read_sql_mock.return_value = pd.DataFrame({"foo_id": [1, 2, 3]})
        # results = get_df()
        # read_sql_mock.assert_called_once()
        # self.assertTrue(compareIt(testDataPath1, testDataPath2))
