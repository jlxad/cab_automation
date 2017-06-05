# import unittest
# from framework.helpers.segment_size_helper import *
# from framework.helpers.mysql_helper import *
#
# import logging
# import csv
# import sys
# reload(sys)
# import psycopg2
# sys.setdefaultencoding('utf8')
#
# logger = logging.getLogger("cab.tests.GetSizeForAllBrandsCategoriesBehaviors")
#
# class GetSizeForAllBrandsCategoriesBehaviors(unittest.TestCase):
#
#      cnx = None
#
#      ###################### Countries and Brands ################################
#      #
#      # #Usecase: Find users who visited a brand and lives in country us
#      # def test_brands_country_comb(self):
#      #
#      #     logger.info("### Usecase: Find users who visited brand and lives in country US ###")
#      #
#      #     # Get the list of brands from the xadcms db
#      #     brand_name= dict()
#      #     conn = mysql_connect_prod("xadcms")
#      #     query = "select * from brands where id >10376 and del=0 "
#      #     brands_list = get_all_result(conn,query)
#      #     for row in brands_list:
#      #         brand_name[row['id']] = row['brand_name']
#      #     conn.close()
#      #
#      #     # Get the audience value for every brand
#      #     brand_audience = dict()
#      #     with open('output_brands.csv', 'wb') as output:
#      #
#      #         for key in brand_name:
#      #             writer = csv.writer(output)
#      #             request = {
#      #                  "brand":{"direct":[key]},
#      #                  "country":{"direct":["us"]},
#      #                  "NOT":{"country":["gb"]}
#      #             }
#      #
#      #             count = segment_size_post("AND",request,db_validation=False)
#      #             list1 = []
#      #             list1.append(key)
#      #             list1.append(brand_name[key])
#      #             list1.append(count)
#      #             brand_audience[key] = list1
#      #             writer.writerow([list1[0],list1[1],list1[2]])
#      #
#      #
#      # # #Usecase: Find users who belong to a particular behaviour audience and lives in country us
#      # # def test_behav_audience_country_comb(self):
#      # #
#      # #     logger.info("### Usecase: Find users who belong to a particular behaviour audience and lives in country us ###")
#      # #
#      # #     # Get the list of behaviour audiences from the xadcms db
#      # #     behav_name=dict()
#      # #     conn = mysql_connect_prod("xadcms")
#      # #     query = "select * from behaviours where del=0"
#      # #     behav_list = get_all_result(conn,query)
#      # #     for row in behav_list:
#      # #         behav_name[row['backend_key']] = row['display_text']
#      # #     conn.close()
#      # #
#      # #     # Get the audience value for every audience
#      # #     behav_audience = dict()
#      # #     for key in behav_name:
#      # #         request = {
#      # #              "behavior":{"direct":[key]},
#      # #              "country":{"direct":["us"]},
#      # #              "NOT":{"country":["gb"]}
#      # #         }
#      # #
#      # #         count = segment_size_post("AND",request,db_validation=False)
#      # #         behav_audience[behav_name[key]] = count
#      # #
#      # #     # Writing data to xl
#      # #     with open('output_behav_audience.csv', 'wb') as output:
#      # #      writer = csv.writer(output)
#      # #      for key, value in behav_audience.iteritems():
#      # #       writer.writerow([key, value])
#      # #
#      #Usecase: Find users who visited a category and lives in country us
#      def test_category_country_comb(self):
#
#          logger.info("### Usecase: Find users who visited category and lives in country US ###")
#
#          conn_string = "host='ec2-54-208-222-203.compute-1.amazonaws.com' dbname='xaddb' user='apps' password='x@d4P55'"
#          print "Connecting to database\n	->%s" % (conn_string)
#          # get a connection, if a connect cannot be made an exception will be raised here
#          conn = psycopg2.connect(conn_string)
#
#          # conn.cursor will return a cursor object, you can use this cursor to perform queries
#          cursor = conn.cursor()
#
#          # execute our Query
#          cursor.execute("select * from categories where hide=false limit 1")
#          records = cursor.fetchall()
#          categ_name = dict()
#          for row in records:
#              list=[]
#              list.append(row[4])
#              list.append(row[1])
#              categ_name[row[0]] = list
#              print row
#          conn.close()
#
#         # Get the audience value for every brand
#          with open('categ_final.csv', 'wb') as output:
#              for key in categ_name:
#                  writer = csv.writer(output)
#                  request = {
#                      "category": {"direct": [str(categ_name[key][0])+"|1|3m|None|None"]},
#                      "country": {"direct": ["us"]}
#                  }
#
#                  count = segment_size_post("AND", request, db_validation=False)
#
#                  request1 = {
#                                 "type": "AND",
#                                 "value": [{
#                                     "type": "category",
#                                     "value": {
#                                         "id": str(categ_name[key][0])
#                                     }
#                                 }, {
#                                     "type": "country",
#                                     "value": "us"
#                                 }]
#                             }
#                  API_URL="http://ec2-52-206-109-219.compute-1.amazonaws.com:8050"
#                  request1= json.dumps(request1)
#                  path = API_URL+"/segment_size?query="+str(request1)
#                  response = requests.get(path)
#                  count1 = response.content.json()['num_audience']
#                  diff=count-count1
#                  writer.writerow([key, categ_name[key][0],categ_name[key][1], count,count1,diff])
#
#
#      # def test_brands(self):
#      #     logger.info("### Usecase: Find users who visited category and lives in country US ###")
#      #     conn_string = "host='ec2-54-208-222-203.compute-1.amazonaws.com' dbname='xaddb' user='apps' password='x@d4P55'"
#      #     print "Connecting to database\n	->%s" % (conn_string)
#      #     # get a connection, if a connect cannot be made an exception will be raised here
#      #     conn = psycopg2.connect(conn_string)
#      #
#      #     # conn.cursor will return a cursor object, you can use this cursor to perform queries
#      #     cursor = conn.cursor()
#      #
#      #     # execute our Query
#      #     cursor.execute("select * from brands where hide=false and id=4004")
#      #     records = cursor.fetchall()
#      #     categ_name = dict()
#      #     for row in records:
#      #         list = []
#      #         list.append(row[1])
#      #         categ_name[row[0]] = list
#      #     conn.close()
#      #
#      #     # Get the audience value for every brand
#      #     with open('brand_final_4.csv', 'wb') as output:
#      #         for key in categ_name:
#      #             writer = csv.writer(output)
#      #             request = {
#      #                 "brand": {"direct": [str(key)+"|1|3m|None|None"]},
#      #                 "country": {"direct": ["us"]},
#      #                 "NOT":{"country":["gb"]}
#      #             }
#      #
#      #             count = segment_size_post("AND",request,db_validation=False)
#      #             writer.writerow([key, categ_name[key][0], count])
#
# if __name__ == '__main__':
#     unittest.main()