import unittest
from framework.helpers.segment_size_helper import *
import logging

logger = logging.getLogger("cab.tests.segmentSizePostTests")

class SegmentSizePostTests(unittest.TestCase):

    cnx = None

    # ###################### Countries ################################
    #
    # # Find users who live in country US
    # def test_users_in_country_us(self):
    #
    #     logger.info("### Usecase: Find users who lives in USA ###")
    #     request = {
    #         "country": {"direct": ["us"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in country Canada
    # def test_users_in_country_cn(self):
    #
    #     logger.info("### Usecase: Find users who lives in Canada ###")
    #     request = {
    #         "country": {"direct": ["cn"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in Great Britain
    # def test_users_in_country_gb(self):
    #
    #     logger.info("### Usecase: Find users who lives in Great Britain ###")
    #     request = {
    #         "country": {"direct": ["gb"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    #
    # ##################### States ######################################
    #
    # # Find users who live in California
    # def test_users_in_state_ca(self):
    #
    #     logger.info("### Usecase: Find users who lives in California ###")
    #     request = {
    #         "state": {"direct": ["ca"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in Arizona
    # def test_users_in_state_az(self):
    #
    #     logger.info("### Usecase: Find users who lives in Arizona ###")
    #     request = {
    #         "state": {"direct": ["az"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in Arizona or in California
    # def test_users_in_state_az_or_in_ca(self):
    #
    #     logger.info("### Usecase: Find users who lives in Arizona or in California ###")
    #     request = {
    #         "OR": {"state": ["az",  "ca"]}
    #     }
    #
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in Arizona or in California but not in Colorado
    # def test_users_in_state_az_or_in_ca_but_not_in_co(self):
    #
    #     logger.info("### Usecase: Find users who lives in Arizona or in California but not in Colorado ###")
    #     request = {
    #         "OR": {"state": ["az", "ca"]},
    #         "NOT": {"state": ["co"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # # Find users who live in California but not in Arizona
    # def test_users_in_state_ca_but_not_in_az(self):
    #
    #     logger.info("### Usecase: Find users who lives in California but not in Arizona ###")
    #     request = {
    #         "state": {"direct": ["ca"]},
    #         "NOT": {"state": ["az"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    #
    #     ###################### Dma ##########################################
    #
    # # Find users who live in DMA "los angeles"
    # def test_users_in_dma_los_angeles(self):
    #
    #     logger.info("### Usecase: Find users who lives in DMA - Los Angeles ###")
    #     request = {
    #         "dma": {"direct": ["803"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in DMA "New york"
    # def test_users_in_dma_new_york(self):
    #
    #     logger.info("### Usecase: Find users who lives in DMA - New York ###")
    #     request = {
    #         "dma": {"direct": ["501"]}
    #     }
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find users who live in DMA "New york" or in DMA "los angeles"
    # def test_users_in_dma_new_york_or_los_angeles(self):
    #
    #     logger.info("### Usecase: Find users who lives in DMA - New York or in Los Angeles ###")
    #     request = {
    #         "OR": {"dma": ["501","803"]}
    #     }
    #
    #     segment_size_post(None,request,db_validation=True)
    #
    # # Find users who live in DMA "los angeles" but not in "San Francisco"
    # def test_users_in_los_angeles_but_not_in_san_francisco(self):
    #
    #     logger.info("### Usecase: Find users who lives in DMA - Los Angeles but not in San Francisco ###")
    #     request = {
    #         "dma": {"direct": ["803"]},
    #         "NOT": {"dma": ["807"]}
    #
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # # Find users who live in DMA "los angeles" or in dma "San Francisco" but not in dma "New York"
    # def test_users_in_los_angeles_or_in_san_francisco_but_not_in_new_york(self):
    #
    #     logger.info("### Usecase: Find users who lives in DMA - Los Angeles or in San Francisco but not in dma New York ###")
    #     request = {
    #         "OR": {"dma": ["803", "807"]},
    #         "NOT": {"dma": ["501"]}
    #
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # ##################### Country and State ###########################
    #
    # # Find users who lives in usa and in california
    # def test_users_in_country_us_and_in_ca(self):
    #
    #     logger.info("### Usecase: Find users who lives in usa and in California ###")
    #     request = {
    #         "state": {"direct": ["ca"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # # Find users who lives in usa and in california or in arizona
    # def test_users_in_country_us_and_in_ca_or_in_az(self):
    #
    #     logger.info("### Usecase: Find users who lives in usa and in California or in Arizona ###")
    #     request = {
    #         "OR": {"state": ["ca", "az"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    #
    # ##################### Country and Dma #############################
    #
    # # Find users who lives in usa and in dma los angeles
    # def test_users_in_country_us_and_in_dma_los_angeles(self):
    #
    #     logger.info("### Usecase: Find users who lives in usa and in dma los angeles ###")
    #     request = {
    #         "dma": {"direct": ["803"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # # Find users who lives in usa and in dma los angeles or in dma new york
    # def test_users_in_country_us_and_in_dma_los_angeles_or_in_dma_new_york(self):
    #
    #     logger.info("### Usecase: Find users who lives in usa and in dma los angeles or in dma New York ###")
    #     request = {
    #         "OR": {"dma": ["803", "501"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    #
    # ##################### Country and State but not DMA ###########################
    #
    # # Find users who lives in usa and in state ca but not in dma los angeles
    # def test_users_in_country_us_and_in_state_ca_but_not_in_dma_los_angeles(self):
    #
    #     logger.info("### Usecase: Find users who lives in usa and in state california but not in dma los angeles ###")
    #     request = {
    #         "NOT": {"dma": ["803"]},
    #         "country": {"direct": ["us"]},
    #         "state": {"direct": ["ca"]}
    #     }
    #
    #     segment_size_post("AND", request, db_validation=True)
    #
    # # Find users who lives in usa and in state ca or in state arizona but not in dma los angeles
    # def test_users_in_country_us_and_in_state_ca_or_in_az_but_not_in_dma_los_angeles(self):
    #
    #     logger.info("### Usecase: Find users who lives in usa and in state california or in state arizona but not in dma los angeles ###")
    #     request = {
    #         "NOT": {"dma": ["803"]},
    #         "country": {"direct": ["us"]},
    #         "OR": {"state": ["ca","az"]}
    #     }
    #
    #     segment_size_post("AND", request, db_validation=True)

    ##################### Brands and Country #######################

    # Find users who visited kfc and lives in country us
    def test_brands_country_comb(self):

        logger.info("### Usecase: Find users who visited kfc and lives in country US ###")
        request = {
            "brand": {"direct": [1]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who visited kfc or mcdonalds and lives in country us
    def test_brands_or_combination(self):

        logger.info("### Usecase: Find users who visited kfc or mcdonalds and lives in country US ###")
        request = {
            "OR": {"brand": [1,25]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who visited kfc and mcdonalds and lives in country us
    def test_brands_and_combination(self):

        logger.info("### Usecase: Find users who visited kfc and mcdonalds and lives in country US ###")
        request = {
            "AND": {"brand": [1,25]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

        #Usecase: Find users who visited kfc and mcdonalds but not tacobell and lives in country us
    def test_brands_and_not_combination(self):

        logger.info("### Usecase: Find users who visited kfc and mcdonalds but not tacobell and lives in country US ###")
        request = {
            "AND": {"brand": [1,25]},
            "country": {"direct": ["us"]},
            "NOT": {"brand": [48]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who visited kfc or mcdonalds but not taco bell and lives in country us
    def test_brands_or_not_combination(self):

        logger.info("### Usecase: Find users who visited kfc or mcdonalds but not taco bell and lives in country US ###")
        request = {
            "OR": {"brand": [1,25]},
            "country": {"direct": ["us"]},
            "NOT": {"brand": [48]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who visited kfc but not mcdonalds and lives in country us
    def test_brands_not_combination(self):

        logger.info("### Usecase: Find users who visited kfc but not mcdonalds and lives in country US ###")
        request = {
            "brand": {"direct": [1]},
            "NOT": {"brand": [25]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    # Usecase : Find users who have visted kfc or mcdonalds and tacobell but not 'burgerking' and lives in country us
    def test_brands_and_or_not_combination(self):

        logger.info("### Usecase: Find users who visited kfc or mcdonalds and tacobell and not burgerking but lives in country us")
        request = {
            "OR": {"direct": [1,25]},
            "brand": {"direct": [48]},
            "NOT": {"brand": [2]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    ##################### Categories and Country #######################

    #Usecase: Find users who belong to category departmental stores lives in country us
    def test_categories_and_country_combination(self):

        logger.info("### Usecase: Find users who belong to category departmental stores lives in country US ###")
        request = {
            "category": {"direct": ["l:531102"]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=False)

    #Usecase: Find users who belong to category departmental stores and restaurants and lives in country us
    def test_categories_and_country_combination(self):

        logger.info("### Usecase: Find users who belong to category departmental stores and restaurants and lives in country US ###")
        request = {
            "AND": {"category": ["l:531102","l:581208"]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who belong to category restaurants or department stores and lives in country us
    def test_category_or_combination(self):

        logger.info("### Usecase: Find users who belong to category restaurants or department stores and lives in country US ###")
        request = {
            "OR": {"category": ["l:531102", "l:581208"]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who belong to category restaurants but not department stores and lives in country us
    def test_categories_not_combination(self):

        logger.info("### Usecase: Find users who belong to category restaurants but not department stores and lives in country US ###")
        request = {
            "category": {"direct": ["l:581208"]},
            "NOT": {"category": ["l:531102"]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who belong to category restaurants and department stores but not movie theaters and lives in country us
    def test_categories_and_not_combination(self):

        logger.info("### Usecase:  Find users who belong to category restaurants and department stores but not movie theaters and lives in country us ###")
        request = {
            "AND": {"category": ["l:531102", "l:581208"]},
            "NOT": {"category": ["l:783201"]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who belong to category restaurants or department stores but not movie theaters and lives in country us
    def test_categories_or_not_combination(self):

        logger.info("### Usecase:  Find users who belong to category restaurants or department stores but not movie theaters and lives in country us ###")
        request = {
            "OR": {"category": ["l:531102", "l:581208"]},
            "NOT": {"category": ["l:783201"]},
            "country": {"direct": ["us"]}
        }

        segment_size_post("AND",request,db_validation=True)

    #Usecase: Find users who belong to category restaurants or department stores and belong to category but not movie theaters and lives in country us
    def test_categories_and_or_not_combination(self):

        logger.info("### Usecase:  Find users who belong to category restaurants or department stores but not movie theaters and lives in country us ###")
        request = {
            "OR": {"category": ["l:531102", "l:581208"]},
            "NOT": {"category": ["l:783201"]},
            "country": {"direct": ["us"]},
            "category": {"direct": ["l:581230"]}
        }

        segment_size_post("AND",request,db_validation=True)

    ##################### Brands and Categories and Country #######################

    # Find users who live in us and visited kfc and belong to category restaurants
    def test_brand_kfc_country_us_and_categ_department_stores(self):
        logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc and lives in country us ###")
        request = {
            "category": {"direct": ["l:581208"]},
            "brand": {"direct": [1]},
            "country": {"direct": ["1"]}
        }

        segment_size_post("AND",request,db_validation=True)

    # Find users who live in us and visited kfc and mcdonalds and belong to category restaurants
    def test_brand_kfc_and_mcdonald_country_us_and_categ_department_stores(self):
        logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc and mcdonalds and lives in country us ###")
        request = {
            "category": {"direct": ["l:581208"]},
            "AND": {"brand": [1,25]},
            "country": {"direct": ["1"]}
        }

        segment_size_post("AND",request,db_validation=True)

    # Find users who live in us and visited kfc and mcdonalds but not visit taco bell and belong to category restaurants
    def test_brand_kfc_and_mcdonald_not_taco_country_us_and_categ_department_stores(self):
        logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc and mcdonalds but not taco bell and lives in country us ###")
        request = {
            "category": {"direct": ["l:581208"]},
            "AND": {"brand": [1,25]},
            "country": {"direct": ["1"]},
            "NOT": {"brand": [48]}
        }

        segment_size_post("AND",request,db_validation=True)

    # Find users who live in us and visited kfc or mcdonalds and belong to category restaurants
    def test_brand_kfc_or_mcdonald_country_us_and_categ_department_stores(self):
        logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc or mcdonalds and lives in country us ###")
        request = {
            "category": {"direct": ["l:581208"]},
            "OR": {"brand": [1,25]},
            "country": {"direct": ["1"]}
        }

        segment_size_post("AND",request,db_validation=True)

    # Find users who live in us and visited kfc or mcdonalds and belong to category restaurants but not visit taco bell
    def test_brand_kfc_or_mcdonald_not_taco_country_us_and_categ_department_stores(self):
        logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc or mcdonalds but not taco and lives in country us ###")
        request = {
            "category": {"direct": ["l:581208"]},
            "OR": {"brand": [1,25]},
            "country": {"direct": ["1"]},
            "NOT": {"brand": [48]}
        }

        segment_size_post("AND",request,db_validation=True)

    # ##################### Behavioural Audiences and Country #######################
    #
    # #Usecase: Find users who belong to behavioural audiences soccer moms and lives in country us
    # def test_behavioural_audiences_and_country_combination(self):
    #
    #     logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms and lives in country us ###")
    #     request = {
    #         "behavior": {"direct": ["soccermoms"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who belong to behavioural audiences soccer moms and dad and lives in country us
    # def test_behavioural_audiences_soccer_moms_and_dad_and_country_combination(self):
    #
    #     logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms and dad and lives in country us ###")
    #     request = {
    #         "AND": {"behavior": ["soccermoms","dad"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who belong to behavioural audiences soccer moms or dad and lives in country us
    # def test_behavioural_audiences_soccer_moms_or_dad_and_country_combination(self):
    #
    #     logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms or dad and lives in country us ###")
    #     request = {
    #         "OR": {"behavior": ["soccermoms", "dad"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who belong to behavioural audiences soccer moms and not dads and lives in country us
    # def test_behavioural_audiences_and_country_combination(self):
    #
    #     logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms and not dads and lives in country us ###")
    #     request = {
    #         "behavior": {"direct": ["soccermoms"]},
    #         "country": {"direct": ["us"]},
    #         "NOT": {"behavior": ["dad"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    #
    # #Usecase: Find users who live in us and belong to soccer moms or dad and not belong to frequent travellers
    # def test_users_in_us_and_soccer_moms_or_dad_and_not_frequent_travelers(self):
    #
    #     logger.info("### Usecase: Find users who live in US and  belong to behavioural audiences soccer moms or dads and not frequent travelers ###")
    #     request = {
    #         "OR": {"behavior": ["soccermoms","dad"]},
    #         "country": {"direct": ["us"]},
    #         "NOT": {"behavior": ["frequenttravelers"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in us and belong to soccer moms or dad and belong to frequent travellers
    # def test_users_in_us_and_soccer_moms_or_dad_and_are_frequent_travelers(self):
    #
    #     logger.info("### Usecase: Find users who live in US and  belong to behavioural audiences soccer moms or dads and are frequent travelers ###")
    #     request = {
    #         "OR": {"behavior": ["soccermoms","dad"]},
    #         "country": {"direct": ["us"]},
    #         "behavior": {"direct": ["frequenttravelers"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in us and belong to soccer moms or dad and belong to frequent travellers but not business travelers
    # def test_users_in_us_and_soccer_moms_or_dad_and_are_frequent_travelers_and_not_business_travelers(self):
    #
    #     logger.info("### Usecase: Find users who live in US and belong to behavioural audiences soccer moms or dads and are frequent travelers but"
    #                 "not business travelers ###")
    #     request = {
    #         "OR": {"behavior": ["soccermoms","dad"]},
    #         "country": {"direct": ["us"]},
    #         "behavior": {"direct": ["frequenttravelers"]},
    #         "NOT":{"behavior":["bt"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    #
    # ##################### Gender and Country #######################
    #
    # # Find all the male users
    # def test_gender_male(self):
    #
    #     logger.info("### Usecase:  Find users of gender male ###")
    #     request = {
    #         "gender": {"direct": ["m"]}
    #     }
    #
    #     segment_size_post(None,request,db_validation=False)
    #
    # # Find all the female users
    # def test_gender_female(self):
    #
    #     logger.info("### Usecase:  Find users of gender female ###")
    #     request = {
    #         "gender": {"direct": ["f"]}
    #     }
    #
    #     segment_size_post(None,request,db_validation=False)
    #
    # #Usecase: Find users of gender male and lives in country us
    # def test_gender_male_and_country(self):
    #
    #     logger.info("### Usecase:  Find users of gender male and lives in country us ###")
    #     request = {
    #         "gender": {"direct": ["m"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # #Usecase: Find users of gender female and lives in country us
    # def test_gender_female_and_country(self):
    #
    #     logger.info("### Usecase:  Find users of gender female and lives in country us ###")
    #
    #     request = {
    #         "gender": {"direct": ["f"]},
    #         "country": {"direct": ["us"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=False)

    # ####################### Custom Audiences and Country #######################
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='214991'
    # def test_country_and_segments(self):
    #
    #     logger.info("### Usecase:  Find users who live in country US and belong to custom audience seg='202551' ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "segment": {"direct": ["202551"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='94167' or seg='93767'
    # def test_country_and_segments_with_or(self):
    #
    #     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg='94167' or seg='93767 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "OR": {"segment": ["94167","93767"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='94167' and not seg='93767'
    # def test_country_and_segments_with_not(self):
    #
    #     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg='94167' and not seg='93767' ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "segment": {"direct": ["94167"]},
    #         "NOT": {"segment": ["93767"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='214991' and seg='214996'
    # def test_country_and_segments_with_and(self):
    #
    #     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg='214991' and seg='214996' ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "AND": {"segment": ["214991","214996"]},
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='214991' and seg='214996'and not seg="215001"
    # def test_country_and_segments_with_and_not(self):
    #
    #     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg='214991' and seg='214996' and not seg='215001' ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "AND": {"segment": ["214991","214996"]},
    #         "NOT": {"segment": ["215001"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='214991' or seg='214996'and not seg="215001"
    # def test_country_and_segments_with_and_not(self):
    #
    #     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg='214991' or seg='214996' and not seg='215001' ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "OR": {"segment": ["214991","214996"]},
    #         "NOT": {"segment": ["215001"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who live in country US and belong to custom audience seg='214991' or seg='214996'and not seg="215001" and seg="215006"
    # def test_country_and_segments_with_and_or_not(self):
    #
    #     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg='215006' and seg='214991' or seg='214996' and not seg='215001' ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "OR": {"segment": ["214991","214996"]},
    #         "NOT": {"segment": ["215001"]},
    #         "segment":{"direct": ["215006"]}
    #     }
    #
    #     segment_size_post("AND",request,db_validation=True)
    #
    #
    #
    # ################################### Age ######################################
    #
    # def test_age_13to17_or_18to24(self):
    #
    #     logger.info("### Usecase: Find users of age 13 to 17 or 18 to 24 ###")
    #     request = {
    #         "country":{"direct":["us"]},
    #         "OR": {"age": [1, 2]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_13to17_or_18to24_or_25to34(self):
    #
    #     logger.info("### Usecase: Find users of age 13 to 17 or 18 to 24 or 25to34 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "OR": {"age": [1, 2, 3]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_13_to_17(self):
    #
    #     logger.info("### Usecase: Find users of age 13 to 17 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct": [1]}
    #              }
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_18_to_24(self):
    #
    #     logger.info("### Usecase: Find users of age 18 to 24 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct": [2]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_25_to_34(self):
    #
    #     logger.info("### Usecase: Find users of age 25 to 34 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct": [3]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_35_to_44(self):
    #
    #     logger.info("### Usecase: Find users of age 35 to 44 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct": [4]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_45_to_54(self):
    #
    #     logger.info("### Usecase: Find users of age 45 to 54 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct": [5]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_55_to_64(self):
    #
    #     logger.info("### Usecase: Find users of age 55 to 64 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct": [6]}}
    #
    #     segment_size_post("AND",request,db_validation=False)
    #
    # def test_age_greater_than_65(self):
    #
    #     logger.info("### Usecase: Find users of age greater than 64 ###")
    #     request = {
    #         "country": {"direct": ["us"]},
    #         "age": {"direct":  [7]}}
    #
    #     segment_size_post("AND",request,db_validation=False)

    ########################################### Multiple Attributes ####################################################

    # Find users who lives in country 'us' and state california but not dma los'angeles' , of gender female, of age 18-24 or 25-34 ,
        # and of behavior soccer moms and visited walmart and belong to category departmental stores
        # and of custom audience 'DLX Auto powered by Polk: Max In Market: All  (iOS)'

    def test_multi_attribute_test1(self):

        logger.info("Find users who lives in country 'us' and state california but not dma los'angeles' , of gender female, of age 18-24 or 25-34 ,"
                    "and of behavior soccer moms and visited walmart and belong to category departmental stores"
                    "and of custom audience DLX Auto powered by Polk: Max In Market: All  (iOS)")

        request = {
                    "country": {"direct": ["us"]},
                    "OR": {"age": [2, 3]},
                    "gender": {"direct": ["f"]},
                    "NOT": {"dma": ["803"]},
                    "state": {"direct": ["ca"]},
                    "segment": {"direct": ["214991"]},
                    "behavior": {"direct": ["soccermoms"]},
                    "brand": {"direct": [1]},
                    "category": {"direct": [531102]}
        }
        segment_size_post("AND",request,db_validation=False)


if __name__ == '__main__':
    unittest.main()
