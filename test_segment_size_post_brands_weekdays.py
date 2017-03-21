import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.segment_size_helper import data_provider
import logging

logger = logging.getLogger("cab.tests.segmentSizePostBrandsWeekdayTests")

class SegmentSizePostBrandsWeekdayTests(unittest.TestCase):

     cnx = None

     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-morning, dayofweek-weekdays ######################################

     freq = lambda: ((1,),(5,),(10,))
     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekdays_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekdays and on mornings")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekdays_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekdays and on mornings")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekdays_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekdays and on mornings")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekdays_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekdays and on mornings")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|1|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-afternoon, dayofweek-weekdays ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekdays_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekdays and on afternoon")

        request = {
            "brand":{ "direct": ["1|"+str(fre)+"|6m|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekdays_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekdays and on afternoon")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekdays_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekdays and on afternoon")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekdays_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekdays and on afternoon")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|2|1"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-evening, dayofweek-weekdays ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekdays_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekdays and on evening")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekdays_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekdays and on evening")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekdays_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekdays and on evening")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekdays_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekdays and on evening")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|3|1"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-night, dayofweek-weekdays ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekdays_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekdays and on night")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekdays_night(self,fre):

        logger.info(" Find users who visited kfc "+str(fre)+"times in last month and on weekdays and on night")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekdays_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekdays and on night")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekdays_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekdays and on night")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|4|1"]}

        }

        segment_size_post(None, request, db_validation=True)



if __name__ == '__main__':
    unittest.main()
