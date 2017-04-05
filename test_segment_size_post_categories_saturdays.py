import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.segment_size_helper import data_provider
from config import *
import logging

logger = logging.getLogger("cab.tests.segmentSizePostCategorysSaturdayTests")

class SegmentSizePostCategorySaturdayTests(unittest.TestCase):

     cnx = None

     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-morning, dayofweek-saturday ######################################

     freq = lambda: ((1,),(5,),(10,))
     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_saturday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on saturday and on mornings")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|1|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_saturday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on saturday and on mornings")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|1|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_saturday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on saturday and on mornings")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|1|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_saturday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on saturday and on mornings")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|1|3"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-afternoon, dayofweek-saturday ######################################

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_saturday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on saturday and on afternoon")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|2|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_saturday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on saturday and on afternoon")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|2|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_saturday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on saturday and on afternoon")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|2|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_saturday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on saturday and on afternoon")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|2|3"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-evening, dayofweek-saturday ######################################

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_saturday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on saturday and on evening")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|3|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_saturday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on saturday and on evening")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|3|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_saturday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on saturday and on evening")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|3|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_saturday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on saturday and on evening")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|3|3"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-night, dayofweek-saturday ######################################

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_saturday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on saturday and on night")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|4|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_saturday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on saturday and on night")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|4|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_saturday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on saturday and on night")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|4|3"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_saturday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on saturday and on night")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|4|3"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs) ######################################


     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter")
        request = {
            "category": {"direct": [category_id+"|"+str(fre)+"|1q|None|None"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_year(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter")
        request = {
            "brand": {"direct": [category_id+"|"+str(fre)+"|1y|None|None"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month")
        request = {
            "brand": {"direct": [category_id+"|"+str(fre)+"|1m|None|None"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6months(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months")
        request = {
            "brand": {"direct": [category_id+"|"+str(fre)+"|6m|None|None"]}

        }

        segment_size_post(None, request, db_validation=True)

if __name__ == '__main__':
    unittest.main()
