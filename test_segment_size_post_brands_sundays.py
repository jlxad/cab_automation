import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.segment_size_helper import data_provider
import logging

logger = logging.getLogger("cab.tests.segmentSizePostBrandsSundayTests")

class SegmentSizePostBrandsSundayTests(unittest.TestCase):

     cnx = None

     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-morning, dayofweek-sunday ######################################

     freq = lambda: ((1,),(5,),(10,))
     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_sunday_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on sunday and on mornings")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|1|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_sunday_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 month and on sunday and on mornings")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|1|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_sunday_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on sunday and on mornings")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|1|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_sunday_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on sunday and on mornings")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|1|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-afternoon, dayofweek-sunday ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_sunday_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on sunday and on afternoon")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|2|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_sunday_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on sunday and on afternoon")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|2|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_sunday_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on sunday and on afternoon")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|2|4"]}
        }

        segment_size_post(None,request,db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_sunday_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on sunday and on afternoon")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|2|4"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-evening, dayofweek-sunday ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_sunday_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on sunday and on evening")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|3|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_sunday_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on sunday and on evening")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|3|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_sunday_evening(self,fre):

        logger.info(" Find users who visited kfc "+str(fre)+"times in last 1 year and on sunday and on evening")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|3|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_sunday_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on sunday and on evening")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|3|4"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-night, dayofweek-sunday ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_sunday_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on sunday and on night")

        request = {
            "brand": {"direct": ["1|"+str(fre)+"|6m|4|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_sunday_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on sunday and on night")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1m|4|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_sunday_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on sunday and on night")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1y|4|4"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_sunday_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on sunday and on night")
        request = {
            "brand": {"direct": ["1|"+str(fre)+"|1q|4|4"]}

        }

        segment_size_post(None, request, db_validation=True)


if __name__ == '__main__':
    unittest.main()
