from unittest import TestCase

from src.py.JsonExtractor import extractJson


class Test(TestCase):
    def test_should_return_one_element_with_CntrNum_key_and_ContainerRec_Values_given_one_cntr_num(self):
        jsonData = {'Message-PSACOPRAR': {'GroupRecord-Container_Group':
                                              [{'Record-ContainerRec': {'Field-CntNo': 'OOLU123',
                                                                        'Field-UnloCode': 'WIGHK'}}]
                                          }}
        self.assertEqual(extractJson(jsonData), {'OOLU123': {'Field-CntNo': 'OOLU123', 'Field-UnloCode': 'WIGHK'}})

    def test_should_return_0_element_given_no_ContainerRec(self):
        jsonData = {'Message-PSACOPRAR': {'GroupRecord-Container_Group': []}}
        self.assertEqual(extractJson(jsonData), {})

    def test_should_return_three_element_with_CntrNum_key_and_ContainerRec_Values_given_three_cntr_num(self):
        jsonData = {'Message-PSACOPRAR': {'GroupRecord-Container_Group':
                                              [{'Record-ContainerRec': {'Field-CntNo': 'OOLU12325',
                                                                        'Field-UnloCode': 'WIGHK'}},
                                               {'Record-ContainerRec': {'Field-CntNo': 'OOLU12335',
                                                                        'Field-UnloCode': 'WIGHK'}},
                                               {'Record-ContainerRec': {'Field-CntNo': 'OOLU12341',
                                                                        'Field-UnloCode': 'WIGHK'}}]
                                          }}
        self.assertEqual(extractJson(jsonData), {
            'OOLU12325': {'Field-CntNo': 'OOLU12325', 'Field-UnloCode': 'WIGHK'},
            'OOLU12335': {'Field-CntNo': 'OOLU12335', 'Field-UnloCode': 'WIGHK'},
            'OOLU12341': {'Field-CntNo': 'OOLU12341', 'Field-UnloCode': 'WIGHK'}})
