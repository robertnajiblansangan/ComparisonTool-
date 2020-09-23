from unittest import TestCase
from src.py.XMLFileExtractor import extractXml


class Test(TestCase):
    def test_should_return_valid_dictionary_given_xml_file_with_no_namespaces(self):
        testDataPath = 'testData/PSA'
        self.assertTrue(extractXml(testDataPath))

    def test_should_return_valid_dictionary_given_xml_file_with_namespaces(self):
        testDataPath = 'testData/PSA2'
        self.assertTrue(extractXml(testDataPath))
