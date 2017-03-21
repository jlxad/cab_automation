# import unittest
# from framework.helpers.segment_size_helper import *
# from framework.helpers.segment_save_helper import *
# import logging
#
# logger = logging.getLogger("cab.tests.segmentSavePostTests")
#
# class SegmentSavePostTests(unittest.TestCase):
#
#      cnx = None
#
#      # ##################### Brands and Country #######################
#      #
#      # #Usecase: Find users who visited kfc and mcdonalds and lives in country us
#      # def test_brands_and_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who visited kfc and mcdonalds and lives in country US ###")
#      #     request = {
#      #          "AND":{"brand":["1","25"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_save_post("AND",request)
#      #
#      # # #Usecase: Find users who visited kfc or mcdonalds and lives in country us
#      # def test_brands_or_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who visited kfc or mcdonalds and lives in country US ###")
#      #     request = {
#      #          "OR":{"brand":["1","25"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who visited kfc but not mcdonalds and lives in country us
#      # def test_brands_not_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who visited kfc but not mcdonalds and lives in country US ###")
#      #     request = {
#      #          "brand":{"direct":["1"]},
#      #          "NOT":{"brand":["25"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who visited kfc ,mcdonalds but not burgerking or starbucks and lives in country us
#      # def test_brands_not_or_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who visited kfc ,mcdonalds but not burgerKing or starbucks and lives in country us ###")
#      #     request = {
#      #          "AND":{"brand":["1","25"]},
#      #          "NOT":{"brand":["2","24"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # ##################### Categories and Country #######################
#      #
#      # #Usecase: Find users who belong to category restaurants and fine dining and lives in country us
#      # def test_categories_and_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who belong to category restaurants and fine dining and lives in country US ###")
#      #     request = {
#      #          "AND":{"category":["l:581208","l:581235"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who belong to category restaurants or fine dining and lives in country us
#      # def test_category_or_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who belong to category restaurants or fine dining and lives in country US ###")
#      #     request = {
#      #          "OR":{"category":["l:581208","l:581235"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who belong to category restaurants but not fine dining and lives in country us
#      # def test_categories_not_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who belong to category restaurants but not fine dining and lives in country US ###")
#      #     request = {
#      #          "category":{"direct":["l:581208"]},
#      #          "NOT":{"category":["l:581235"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who belong to category restaurants and fine dining but not movie theaters and entertainment bureau and lives in country us
#      # def test_categories_not_or_combination(self):
#      #
#      #     logger.info("### Usecase:  Find users who belong to category restaurants and fine dining but not movie theaters and entertainment bureau and lives in country us ###")
#      #     request = {
#      #          "AND":{"category":["l:581208","l:581235"]},
#      #          "NOT":{"category":["l:783201","l:792905"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      #
#      # ##################### Behavioural Audiences and Country #######################
#      #
#      # #Usecase: Find users who belong to behavioural audiences vda and millennials and lives in country us
#      # def test_behavioural_audiences_and_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who belong to behavioural audiences vda and millennials and lives in country us ###")
#      #     request = {
#      #          "AND":{"behavior":["vda","millennials"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who belong to behavioural audiences millennials or vda and lives in country us
#      # def test_behavioural_audience_or_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who belong to behavioural audiences millennials or vda and lives in country us ###")
#      #     request = {
#      #          "OR":{"behavior":["vda","millennials"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who belong to behavioural audience vda but not millennials and lives in country us
#      # def test_behavioural_audience_not_combination(self):
#      #
#      #     logger.info("### Usecase: Find users who belong to behavioural audience vda but not millennials and lives in country us ###")
#      #     request = {
#      #          "behavior":{"direct":["vda"]},
#      #          "NOT":{"behavior":["millennials"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users who belong to behavioural audience vda, millennials but not gz and bt and lives in country us
#      # def test_behavioural_audience_not_or_combination(self):
#      #
#      #     logger.info("### Usecase:  Find users who belong to behavioural audience vda, millennials but not gz and bt and lives in country us ###")
#      #     request = {
#      #          "AND":{"behavior":["vda","millennials"]},
#      #          "NOT":{"behavior":["gz","bt"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # ##################### Gender and Country #######################
#      #
#      # #Usecase: Find users of gender male and lives in country us
#      # def test_gender_male_and_country(self):
#      #
#      #     logger.info("### Usecase:  Find users of gender male and lives in country us ###")
#      #     request = {
#      #          "gender":{"direct":["m"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      # #Usecase: Find users of gender female and lives in country us
#      # def test_gender_female_and_country(self):
#      #
#      #     logger.info("### Usecase:  Find users of gender female and lives in country us ###")
#      #     request = {
#      #          "gender":{"direct":["f"]},
#      #          "country":{"direct":["us"]}
#      #     }
#      #
#      #     segment_size_post("AND",request)
#      #
#      ##################### Custom Audiences and Country #######################
#
#      #Usecase: Find users who live in country US and belong to custom audience seg1='94167'
#      def test_country_and_segments(self):
#
#          logger.info("### Usecase:  Find users who live in country US and belong to custom audience seg1='94167' ###")
#          request = {
#               "country":{"direct":["us"]},
#               "segment":{"direct":["94167"]}
#          }
#
#          segment_size_post("AND",request)
#
#      #Usecase: Find users who live in country US and belong to custom audience seg1='94167' or seg='93767'
#      def test_country_and_segments_with_or(self):
#
#          logger.info("### Usecase:Find users who live in country US and belong to custom audience seg1='94167' or seg='93767 ###")
#          request = {
#               "country":{"direct":["us"]},
#               "OR":{"segment":["94167","93767"]}
#          }
#
#          segment_size_post("AND",request)
#
#
#      # ####################################### Geotargets ###############################################
#      #
#      # def test_countries_or(self):
#      #     logger.info("### Usecase:  Find users who lives in country us or in gb ###")
#      #     request = {
#      #          "OR":{"country":["us","gb"]}
#      #     }
#      #
#      #     segment_size_post(None,request)
#      #
#      #
#      #
#      # ####################################### Basic Conditions #########################################
#      #
#      # #Usecase: Find users who live in country US
#      # def test_country(self):
#      #
#      #     logger.info("### Usecase:Find users who live in country US ###")
#      #
#      #     segment_size_post_single_object("country","us")
#      #
#      # #Usecase: Find users who visited brand Kfc
#      # def test_brand(self):
#      #
#      #     logger.info("### Usecase:Find users who visited brand Kfc ###")
#      #
#      #     segment_size_post_single_object("brand","1")
#      #
#      # #Usecase: Find users who belong to category Restaurants
#      # def test_category(self):
#      #
#      #     logger.info("### Usecase:Find users who belong to category Restaurants ###")
#      #
#      #     segment_size_post_single_object("category","l:581208")
#      #
#      # #Usecase: Find users of gender male
#      # def test_gender(self):
#      #
#      #     logger.info("### Usecase:Find users of gender male ###")
#      #
#      #     segment_size_post_single_object("gender","m")
#      #
#      # #Usecase: Find users of behavioural audience vda
#      # def test_behavioural_audience(self):
#      #
#      #     logger.info("### Usecase:Find users of behavioural audience vda ###")
#      #
#      #     segment_size_post_single_object("behavior","vda")
#      #
#      # #Usecase: Find users of custom audience seg= "94167"
#      # def test_custom_audience(self):
#      #
#      #     logger.info("### Usecase:Find users of custom audience seg=94167 ###")
#      #
#      #     segment_save_post_single_object("segment","94167")
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()
