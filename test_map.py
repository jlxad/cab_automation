import unittest
from framework.helpers.build_dictionary_helper import *
from framework.helpers.segment_size_helper import *
import logging
import sys
reload(sys)
import dill
import os

sys.setdefaultencoding('utf8')

logger = logging.getLogger("cab.tests.GetSizeForAllBrandsCategoriesBehaviors")


class GetMap(unittest.TestCase):

    cnx = None

    # def test_country_map(self):
    #     country_dict = create_country_map()
    #     dill.dump.txt(country_dict,open("country","w"),-1)
    #     country_dict_final = dict()
    #     country_dict_final = dill.load(open("country"))
    #     print country_dict_final['ca']


    # def test_brands(self):
    #
    #     brand_list= create_brand_categ_map('brand')
    #     dill.dump.txt(brand_list,open("brand","w"))


    # def test_func(self):
    #     country_dict_final = dill.load(open("country"))
    #     brand_dict_final = dill.load(open("brand"))
    #     list1 = []
    #     list2 = []
    #     # list1=country_dict_final['us']
    #     list2 = brand_dict_final['0,yr_1,1']
    #
    #     print len(list2)



    # def test_print_map(self):
    #     print create_dictionary_from_file('/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/dump.txt')
    #     country_map =dict()
    #     country_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/country.txt"))
    #     print country_map['us']

    # def test_sample(self):
    #     # create_dictionary_from_file('/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/dump.txt')
    #     category_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/category.txt"))
    #     print len(category_map['581208,yr:tod_1:2'][5])
    #     # print len(brand_map['1,yr_1'][1])
    #     # print len(brand_map['1,yr_1'][5])
    #     # print len(brand_map['1,yr_1'][10])
    #
    #     # print len(gender_map['f'])
    #     request2 = {
    #         "type": "category","value": {"id": 581208,"duration": "1m","timeofday": 1,"dayofweek":None,"minfreq": 1}
    #
    #     }
    #     path = API_URL + "/segment_size?query="+str(json.dumps(request2))
    #     response = requests.get(path)
    #     print response.content
    #     print response.json()['num_audience']

    def test_sample_1(self):
         fileDir = os.path.dirname(os.path.realpath('__file__'))
         print fileDir


if __name__ == '__main__':
    unittest.main()
