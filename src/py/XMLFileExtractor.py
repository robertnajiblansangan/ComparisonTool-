import os, glob
import xmltodict

from lxml import etree

from src.py.JsonExtractor import extractJson


def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def extractXml(folder_path):
    newTliDataDict = {}
    for filename in glob.glob(os.path.join(folder_path, '*')):
        with open(filename, 'rb') as openedFile:
            try:
                root = etree.fromstring(openedFile.read())

                # Remove namespace prefixes
                for elem in root.getiterator():
                    elem.tag = etree.QName(elem).localname

                etree.cleanup_namespaces(root)

                json_data = xmltodict.parse(etree.tostring(root).decode().replace(' DataType="String"', '')
                                            , xml_attribs=True)
                newTliDataDict = merge(newTliDataDict, extractJson(json_data))
            except:
                print("An exception occured")
    return newTliDataDict
