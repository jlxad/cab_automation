import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.mysql_helper import *
import logging
import csv

logger = logging.getLogger("cab.tests.GetSizeForAllBrandsCategoriesBehaviors")

class GetSizeForAllBrandsCategoriesBehaviors(unittest.TestCase):

     cnx = None

     ###################### Countries and Brands ################################

     #Usecase: Find users who visited a brand and lives in country us
     def test_brands_country_comb(self):

         logger.info("### Usecase: Find users who visited brand and lives in country US ###")

         # Get the list of brands from the xadcms db
         brand_name= dict()
         conn = mysql_connect_prod("xadcms")
         query = "select * from brands where id >10376 and del=0 "
         brands_list = get_all_result(conn,query)
         for row in brands_list:
             brand_name[row['id']] = row['brand_name']
         conn.close()

         # Get the audience value for every brand
         brand_audience = dict()
         with open('output_brands.csv', 'wb') as output:

             for key in brand_name:
                 writer = csv.writer(output)
                 request = {
                      "brand":{"direct":[key]},
                      "country":{"direct":["us"]},
                      "NOT":{"country":["gb"]}
                 }

                 count = segment_size_post("AND",request,db_validation=False)
                 list1 = []
                 list1.append(key)
                 list1.append(brand_name[key])
                 list1.append(count)
                 brand_audience[key] = list1
                 writer.writerow([list1[0],list1[1],list1[2]])


     # #Usecase: Find users who belong to a particular behaviour audience and lives in country us
     # def test_behav_audience_country_comb(self):
     #
     #     logger.info("### Usecase: Find users who belong to a particular behaviour audience and lives in country us ###")
     #
     #     # Get the list of behaviour audiences from the xadcms db
     #     behav_name=dict()
     #     conn = mysql_connect_prod("xadcms")
     #     query = "select * from behaviours where del=0"
     #     behav_list = get_all_result(conn,query)
     #     for row in behav_list:
     #         behav_name[row['backend_key']] = row['display_text']
     #     conn.close()
     #
     #     # Get the audience value for every audience
     #     behav_audience = dict()
     #     for key in behav_name:
     #         request = {
     #              "behavior":{"direct":[key]},
     #              "country":{"direct":["us"]},
     #              "NOT":{"country":["gb"]}
     #         }
     #
     #         count = segment_size_post("AND",request,db_validation=False)
     #         behav_audience[behav_name[key]] = count
     #
     #     # Writing data to xl
     #     with open('output_behav_audience.csv', 'wb') as output:
     #      writer = csv.writer(output)
     #      for key, value in behav_audience.iteritems():
     #       writer.writerow([key, value])
     #
     #Usecase: Find users who visited a category and lives in country us
     def test_category_country_comb(self):

         logger.info("### Usecase: Find users who visited category and lives in country US ###")

         # Get the list of brands from the xadcms db
         categ_name= dict()
         conn = mysql_connect_prod("xadcms")
         query = "select * from category where del=0 "
         categ_list = get_all_result(conn,query)
         for row in categ_list:
             list=[]
             list.append(row['id'])
             list.append(row['name'])
             categ_name[row['sicCode']] = list
         conn.close()

         # Get the audience value for every brand
         categ_audience = dict()
         with open('output_category.csv', 'wb') as output:

             for key in categ_name:
                 writer = csv.writer(output)
                 request = {
                      "category":{"direct":["l:"+str(key)]},
                      "country":{"direct":["us"]},
                      "NOT":{"country":["gb"]}
                 }

                 count = segment_size_post("AND",request,db_validation=False)
                 list1 = []
                 list1.append(key)
                 val = categ_name[key]
                 list1.append(val[0])
                 list1.append(val[1])
                 list1.append(count)
                 categ_audience[key] = list1
                 writer.writerow([list1[1],list1[0],list1[2],list1[3]])

if __name__ == '__main__':
    unittest.main()