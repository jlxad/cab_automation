import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.segment_size_helper import data_provider
import logging

logger = logging.getLogger("cab.tests.segmentSizePostCategoryWeekdayTests")

class SegmentSizePostCategoryWeekdayTests(unittest.TestCase):

     cnx = None

     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-morning, dayofweek-weekday ######################################

     freq = lambda:((1,),(5,),(10,))
     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_weekday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on weekday and on mornings")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_weekday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on weekday and on mornings")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_weekday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on weekday and on mornings")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_weekday_morning(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on weekday and on mornings")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-afternoon, dayofweek-weekday ######################################

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_weekday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on weekday and on afternoon")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_weekday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on weekday and on afternoon")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_weekday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on weekday and on afternoon")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_weekday_afternoon(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on weekday and on afternoon")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-evening, dayofweek-weekday ######################################

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_weekday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on weekday and on evening")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|3|1"]}

        }

        segment_size_post(None, request ,db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_weekday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on weekday and on evening")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_weekday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on weekday and on evening")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1y|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_weekday_evening(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on weekday and on evening")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Category Combination - freq-(1,5,10),duration(all combs), timeofday-night, dayofweek-weekday ######################################

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_6_months_on_weekday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 6 months and on weekday and on night")

        request = {
            "category": {"direct": ["581208|"+str(fre)+"|6m|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_month_on_weekday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last month and on weekday and on night")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1m|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_fre_x_in_last_1_year_on_weekday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last 1 year and on weekday and on night")
        request = {
            "category":{"direct": ["581208|"+str(fre)+"|1y|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_restaurants_of_freq_x_in_last_quarter_on_weekday_night(self,fre):

        logger.info("Find users who visited restaurants "+str(fre)+"times in last quarter and on weekday and on night")
        request = {
            "category": {"direct": ["581208|"+str(fre)+"|1q|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)


if __name__ == '__main__':
    unittest.main()
