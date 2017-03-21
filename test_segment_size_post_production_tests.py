import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.prod_data_validation_helper import *
from framework.helpers.prod_data_validation_helper import t
import logging

logger = logging.getLogger("cab.tests.ProductionTests")

class ProductionTests(unittest.TestCase):

 cnx = None

 ###################################### Country ##########################################

 ## Find users who live in US ##
 def test_users_in_us(self):

     query = "Find users who lives in country US"
     logger.info("### Usecase:"+str(query)+" ###")
     count = segment_size_post_single_object("country","us",db_validation=False)
     verify_data_in_db_helper(count,"1",query)

 ## Find users who live in UK ##
 def test_users_in_gb(self):

     query = "Find users who lives in country UK"
     logger.info("### Usecase:"+str(query)+" ###")
     count = segment_size_post_single_object("country","gb",db_validation=False)
     verify_data_in_db_helper(count,"2",query)

 ###################################### Gender & Country ##########################################

 ## Find users who live in US and of gender male ##
 def test_users_in_us_and_male(self):

     query = "Find users who lives in country US and of gender male"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "gender":{"direct":["m"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"3",query)

 ## Find users who live in US and of gender female ##
 def test_users_in_us_and_female(self):

     query = "Find users who lives in country US and of gender female"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "gender":{"direct":["f"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"4",query)

 ## Find users who live in UK and of gender male ##
 def test_users_in_uk_and_male(self):

     query = "Find users who lives in country UK and of gender male"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "gender":{"direct":["m"]},
              "country":{"direct":["gb"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"5",query)

 ## Find users who live in UK and of gender female ##
 def test_users_in_uk_and_female(self):

     query = "Find users who lives in country UK and of gender female"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "gender":{"direct":["f"]},
              "country":{"direct":["gb"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"6",query)

 ###################################### Age & Country - US  ##########################################

 ## Find users who live in US and of age 13-17 ##
 def test_users_in_us_and_age_13_to_17(self):

    query = "Find users who lives in country us and of age 13-17"
    logger.info("### Usecase:"+str(query)+" ###")
    request = {
          "country":{"direct":["us"]},
          "age":{"direct":[1]}}

    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"7",query)

 ## Find users who live in US and of age 18-24 ##
 def test_users_in_us_and_age_18_to_24(self):

     query = "Find users who lives in country us and of age 18-24"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[2]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"8",query)

 ## Find users who live in US and of age 25-34 ##
 def test_users_in_us_and_age_25_to_34(self):

     query = "Find users who lives in country us and of age 25-34"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[3]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"9",query)

 ## Find users who live in US and of age 35-44 ##
 def test_users_in_us_and_age_35_to_44(self):

     query = "Find users who lives in country us and of age 35-44"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[4]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"10",query)

 ## Find users who live in US and of age 45-54 ##
 def test_users_in_us_and_age_45_to_54(self):

     query = "Find users who lives in country us and of age 45-54"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[5]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"11",query)

 ## Find users who live in US and of age 55-64 ##
 def test_users_in_us_and_age_55_to_64(self):

     query = "Find users who lives in country us and of age 55-64"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[6]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"12",query)

 ## Find users who live in US and of age more than 65 ##
 def test_users_in_us_and_age_greater_than_65(self):

     query = "Find users who lives in country us and of age more than 65"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[7]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"13",query)

###################################### Age & Country - GB ##########################################

 ## Find users who live in GB and of age 13-17 ##
 def test_users_in_gb_and_age_13_to_17(self):

    query = "Find users who lives in country gb and of age 13-17"
    logger.info("### Usecase:"+str(query)+" ###")
    request = {
          "country":{"direct":["gb"]},
          "age":{"direct":[1]}}

    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"14",query)

 ## Find users who live in GB and of age 18-24 ##
 def test_users_in_gb_and_age_18_to_24(self):

     query = "Find users who lives in country gb and of age 18-24"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["gb"]},
              "age":{"direct":[2]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"15",query)

 ## Find users who live in GB and of age 25-34 ##
 def test_users_in_gb_and_age_25_to_34(self):

     query = "Find users who lives in country gb and of age 25-34"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["gb"]},
              "age":{"direct":[3]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"16",query)

 ## Find users who live in gb and of age 35-44 ##
 def test_users_in_gb_and_age_35_to_44(self):

     query = "Find users who lives in country gb and of age 35-44"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["gb"]},
              "age":{"direct":[4]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"17",query)

 ## Find users who live in gb and of age 45-54 ##
 def test_users_in_gb_and_age_45_to_54(self):

     query = "Find users who lives in country gb and of age 45-54"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["us"]},
              "age":{"direct":[5]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"18",query)

 ## Find users who live in gb and of age 55-64 ##
 def test_users_in_gb_and_age_55_to_64(self):

     query = "Find users who lives in country gb and of age 55-64"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["gb"]},
              "age":{"direct":[6]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"19",query)

 ## Find users who live in gb and of age more than 65 ##
 def test_users_in_gb_and_age_greater_than_65(self):

     query = "Find users who lives in country gb and of age more than 65"
     logger.info("### Usecase:"+str(query)+" ###")

     request = {
              "country":{"direct":["gb"]},
              "age":{"direct":[7]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"20",query)

 ######################## Brands & Categories #############################

 ## Find users who live in us and visited kfc
 def test_users_in_us_and_visited_kfc(self):

    query = "Find users who lives in country us and visited kfc"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["1"]},
              "country":{"direct":["us"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"21",query)

  # Find users who live in US and visited Burger King
 def test_users_in_usa_and_visited_burger_king(self):

    query = "Find users who lives in country us and visited Burger King"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "brand":{"direct":["2"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"22",query)

  # Find users who live in US and visited Home Depot
 def test_users_in_us_and_visited_home_depot(self):

    query = "Find users who lives in country us and visited Home Depot"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["8"]},
              "country":{"direct":["us"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"23",query)

 # Find users who live in US and visited Walmart Supercenter
 def test_users_in_us_and_visited_walmart_supercenter(self):

    query = "Find users who lives in country us and visited walmart supercenter"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["282"]},
              "country":{"direct":["us"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"24",query)

 # Find users who live in US and visited target
 def test_users_in_usa_and_visited_target(self):

    query = "Find users who lives in country us and visited target"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "brand":{"direct":["10"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"25",query)

 # Find users who live in US and visited mcdonalds
 def test_users_in_us_and_visited_mcdonalds(self):

    query = "Find users who lives in country us and visited mcdonalds"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["25"]},
              "country":{"direct":["us"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"26",query)

 # Find users who live in US and visited taco bell
 def test_users_in_us_and_visited_taco_bell(self):

    query = "Find users who lives in country us and visited taco bell"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["48"]},
              "country":{"direct":["us"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"27",query)

 # Find users who live in US and visited Costco
 def test_users_in_usa_and_visited_costco(self):

    query = "Find users who lives in country us and visited Costco"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "brand":{"direct":["32"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"28",query)

 # Find users who live in US and visited walmart
 def test_users_in_usa_and_visited_walmart(self):

    query = "Find users who lives in country us and visited walmart"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "brand":{"direct":["9"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"29",query)

 # Find users who live in US and belong to category "Automobile Dealers-New Cars"
 def test_users_in_usa_and_category_automobile_dealers_new_cars(self):

    query = "Find users who lives in country us and belong to category Automobile Dealers-New Cars"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "category":{"direct":["l:551102"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"30",query)

 # Find users who live in US and belong to category "Restaurants"
 def test_users_in_usa_and_category_restaurants(self):

    query = "Find users who lives in country us and belong to category Restaurants"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "category":{"direct":["l:581208"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"31",query)

 # Find users who live in US and belong to category "Department Stores"
 def test_users_in_usa_and_category_department_stores(self):

    query = "Find users who lives in country us and belong to category Department Stores"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "category":{"direct":["l:531102"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"32",query)

 # Find users who live in US and belong to category "Pharmacies"
 def test_users_in_usa_and_category_pharmacies(self):

    query = "Find users who lives in country us and belong to category Pharmacies"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "category":{"direct":["l:591205"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"33",query)


 ######################## Country & State #############################

 ## Find users who live in US and belong to state "ca" ##
 def test_users_in_us_and_in_california(self):

     query = "Find users who lives in country US and of state california"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "state":{"direct":["ca"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"34",query)

 ## Find users who live in US and belong to state "ny" ##
 def test_users_in_us_and_in_new_york(self):

     query = "Find users who lives in country US and of state New York"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "state":{"direct":["ny"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"35",query)

 ## Find users who live in US and belong to state "tx" ##
 def test_users_in_us_and_in_texas(self):

     query = "Find users who lives in country US and of state Texas"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "state":{"direct":["tx"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"36",query)

 ######################## Country & State & DMA #############################

 ## Find users who live in US and belong to state "ca" and dma "los angeles" ##
 def test_users_in_us_and_in_california_and_in_dma_los_angeles(self):

     query = "Find users who lives in country US and of state california and in dma los angeles"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "state":{"direct":["ca"]},
              "country":{"direct":["us"]},
              "dma":{"direct":[803]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"37",query)

 ## Find users who live in US and belong to state "ca" and dma "san francisco" ##
 def test_users_in_us_and_in_california_and_in_dma_san_francisco(self):

     query = "Find users who lives in country US and of state california and in dma san francisco"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "state":{"direct":["ca"]},
              "country":{"direct":["us"]},
              "dma":{"direct":[807]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"38",query)

 ## Find users who live in US and belong to state "ny" and dma "new york" ##
 def test_users_in_us_and_in_new_york_and_dma_new_york(self):

     query = "Find users who lives in country US and of state New York and of dma New York"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "state":{"direct":["ny"]},
              "country":{"direct":["us"]},
              "dma":{"direct":[501]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"39",query)

 ######################## Countries & Behavioural Audiences #############################

 ## Find users who live in US and belong to home contractors ##
 def test_users_in_us_and_home_contractors(self):

     query = "Find users who lives in country US and are home contractors"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["con"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"40",query)

 ## Find users who live in US and belong to millennials ##
 def test_users_in_us_and_millennials(self):

     query = "Find users who lives in country US and are millennials"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["millennials"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"41",query)

 ## Find users who live in US and belong to soccer moms ##
 def test_users_in_us_and_soccer_moms(self):

     query = "Find users who lives in country US and are soccermoms"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["soccermoms"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"42",query)

 ## Find users who live in US and belong to hispanics ##
 def test_users_in_us_and_hispanics(self):

     query = "Find users who lives in country US and are hispanics"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["hispanics"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"43",query)

 ## Find users who live in US and belong to sportsenthusiasts ##
 def test_users_in_us_and_sportsenthusiasts(self):

     query = "Find users who lives in country US and are sportsenthusiasts"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["sportsenthusiasts"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"44",query)

 ## Find users who live in US and belong to commuters ##
 def test_users_in_us_and_commuters(self):

     query = "Find users who lives in country US and are commuters"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["com"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"45",query)

 ## Find users who live in US and belong to diys ##
 def test_users_in_us_and_diys(self):

     query = "Find users who lives in country US and are diys"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["diy"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"46",query)

 ## Find users who live in US and belong to golfers ##
 def test_users_in_us_and_golfers(self):

     query = "Find users who lives in country US and are golfers"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["go"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"47",query)

 ## Find users who live in US and belong to dad ##
 def test_users_in_us_and_dad(self):

     query = "Find users who lives in country US and are dad"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["dad"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"48",query)

 ## Find users who live in US and belong to in market for carriers ##
 def test_users_in_us_and_inmarket_for_carriers(self):

     query = "Find users who lives in country US and are in market for carriers"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["ic"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"49",query)

 ## Find users who live in US and belong to big city moms ##
 def test_users_in_us_and_big_city_moms(self):

     query = "Find users who lives in country US and are big city moms"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["umom"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"50",query)

 ## Find users who live in US and belong to in market for furnitures ##
 def test_users_in_us_and_in_market_for_furnitures(self):

     query = "Find users who lives in country US and belong to in market for furnitures"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["if"]},
              "country":{"direct":["us"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"51",query)

 ## Find users who live in Canada and are soccermoms ##
 def test_users_in_cn_and_are_soccermoms(self):

     query = "Find users who lives in country Canada and belong to Soccermoms"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
              "behavior":{"direct":["soccermoms"]},
              "country":{"direct":["cn"]}
         }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"52",query)

 ######################## Combinations #############################

 ## Find users who live in US and belong to soccer moms and of gender female ##
 def test_users_in_usa_and_soccer_moms_and_gender_female(self):

    query = " Find users who live in US and belong to soccer moms and of gender female "
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "behavior":{"direct":["soccermoms"]},
              "country":{"direct":["us"]},
              "gender":{"direct":["f"]}
               }
    count =  segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"53",query)

 ## Find users who live in US and belong to soccer moms and of gender male ##
 def test_users_in_usa_and_soccer_moms_and_gender_male(self):

    query = " Find users who live in US and belong to soccer moms and of gender male"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "behavior":{"direct":["soccermoms"]},
              "country":{"direct":["us"]},
              "gender":{"direct":["m"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"54",query)

 ## Find users who live in US and belong to soccer moms and dad ##
 def test_users_in_usa_and_soccer_moms_and_dad(self):

    query = " Find users who live in US and belong to soccer moms and dad"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "AND":{"behavior":["soccermoms","dad"]},
              "country":{"direct":["us"]},
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"55",query)

 ## Find users who live in US and visited Home Depot and of gender male ##
 def test_users_in_usa_and_visited_home_depot_and_gender_male(self):

    query = "Find users who live in US and visited Home Depot and gender male"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["8"]},
              "country":{"direct":["us"]},
              "gender":{"direct":["m"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"56",query)

 ## Find users who live in US and visited Home Depot and of gender female ##
 def test_users_in_usa_and_visited_home_depot_and_gender_female(self):

    query = "Find users who live in US and visited Home Depot and gender female"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "brand":{"direct":["8"]},
              "country":{"direct":["us"]},
              "gender":{"direct":["f"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"57",query)

 ## Find users who live in US and visited Costco and visited target ##
 def test_users_in_usa_and_visited_costco_and_target(self):

    query = "Find users who live in US and visited Costco and Target"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "AND":{"brand":["32","10"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"58",query)

 ## Find users who live in US and visited target and visited departmental stores ##
 def test_users_in_usa_and_visited_target_and_visited_departmental_stores(self):

    query = "Find users who live in US and visited target and visited departmental stores"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "brand":{"direct":["10"]},
              "category":{"direct":["l:531102"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"59",query)

 ## Find users who live in US and visited KFC and visited Taco Bell and visited mcdonalds ##
 def test_users_in_usa_and_visited_kfc_and_taco_and_mcdonalds(self):

    query = "Find users who live in US and visited kfc and taco bell and mcdonalds"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "AND":{"brand":["1","48","25"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"60",query)

 ## Find users who live in US and visited kfc and taco bell ##
 def test_users_in_usa_and_visited_kfc_and_taco(self):

    query = "Find users who live in US and visited kfc and taco bell"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "AND":{"brand":[1,48]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"61",query)

 ## Find users who live in US and visited KFC or visited Taco Bell ##
 def test_users_in_usa_and_visited_kfc_or_taco(self):

    query = " Find users who live in US and visited KFC or visited Taco Bell"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
              "country":{"direct":["us"]},
              "OR":{"brand":["1","48"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"62",query)

 ## Find users who live in US and belong to business Traveler and visited kfc ##
 def test_users_in_usa_and_business_travellers_and_visited_kfc(self):

    query = "Find users who live in US and belong to business Traveler and visited kfc"
    logger.info("### Usecase:"+str(query)+" ###")
    request = {
              "country":{"direct":["us"]},
              "behavior":{"direct":["bt"]},
              "brand":{"direct":["1"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"63",query)

 ## Find users who live in US and belong to business Traveler and not visited kfc ##
 def test_users_in_usa_and_business_travellers_and_not_visited_kfc(self):

    query = "Find users who live in US and belong to business Traveler and not visited kfc"
    logger.info("### Usecase:"+str(query)+" ###")
    request = {
              "country":{"direct":["us"]},
              "behavior":{"direct":["bt"]},
              "NOT":{"brand":["1"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"64",query)

 ## Find users who live in US and belong to Soccer Moms and who visited Target ##
 def test_users_in_usa_and_soccer_moms_and_visted_target(self):

    query = "Find users who live in US and belong to Soccer Moms and who visited Target"
    logger.info("### Usecase:"+str(query)+" ###")
    request = {
              "behavior":{"direct":["soccermoms"]},
              "country":{"direct":["us"]},
              "brand":{"direct":["10"]}
               }
    count = segment_size_post("AND",request,db_validation=False)
    verify_data_in_db_helper(count,"65",query)

 ## Find users who live in US and belong to Soccer Moms OR who visited target ##
 def test_users_in_usa_and_soccermoms_or_visited_target(self):

    query = "Find users who live in US and belong to soccer moms or visited target"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {"type" : "AND" , "value" : [
                                           {"type" : "country" , "value" : "us" } ,
                                           {"type" : "OR", "value" : [
                                                                                   { "type" : "brand" , "value" : {"id": 10} } ,
                                                                                   { "type" : "behavior" , "value" : "soccermoms" }
                                                                                 ]
                                           }
                                         ]
             }


    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"66",query)

 ## Find users who live in US and belong to Soccer Moms but not visited target ##
 def test_users_in_usa_and_soccermoms_not_visited_target(self):

    query = "Find users who live in US and belong to soccer moms and not visited target"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
        "type": "AND",
        "value": [{"type": "country","value": "us"},
                  {"type": "AND","value": [{"type": "behavior","value": "soccermoms"},
                                           {"type": "NOT","value": {"type": "brand","value": {"id": 10}}}
                                           ]
                  }]
    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"67",query)

 ################# Test cases to verify the operations on the application ######################

 def test_country_and_or_between_states_and_exlude_multiple_dmas(self):

    query = "Find users who live in US and visited states(ca or mn or ny) and exclude (los angeles or minneapolis)"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [
                          {"type": "country","value": "us"},
                          {"type": "OR","value": [{"type": "state","value": "ca"},
                                                  {"type": "state","value": "mn"},
                                                  {"type": "state","value": "ny"}
                                                 ]
                          },
                          {
                           "type": "OR","value": [{"type": "NOT","value": {"type": "dma","value": 803}},
                                                  {"type": "NOT","value": {"type": "dma","value": 613}}]

                          }

                          ]
             }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"68",query)

 def test_country_and_or_between_states_and_dmas(self):

    query = "Find users who live in US and visited (states ca or ny or dma-austin)"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [
                          {"type": "country","value": "us"},
                          {"type": "OR","value": [{"type": "state","value": "ca"},
                                                  {"type": "state","value": "mn"},
                                                  {"type": "dma","value": 635}
                                                 ]
                          }
                          ]
             }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"69",query)

 def test_country_and_or_between_states_and_dmas_and_not_dma(self):

    query = "Find users who live in US and visited (states ca or ny or dma-austin) and not dma-los angeles"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [
                          {"type": "country","value": "us"},
                          {"type": "OR","value": [{"type": "state","value": "ca"},
                                                  {"type": "state","value": "mn"},
                                                  {"type": "dma","value": 635}
                                                 ]
                          },
                          {"type": "NOT","value": {"type": "dma","value": 803}}
                          ]
             }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"70",query)

 def test_brands_or_categ_or_behaviours_and_country_us(self):

    query = "Find users who live in US and visited walmart or restaurants or Golfers"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                "type": "AND",
                "value": [{
                    "type": "country",
                    "value": "us"
                }, {
                    "type": "OR",
                    "value": [{
                        "type": "brand",
                        "value": {
                            "id": 9
                        }
                    }, {
                        "type": "behavior",
                        "value": "go"
                    },
                        {
                        "type": "category",
                        "value": {
                            "id": "581208"
                        }
                    }
                        ]
                }
            ]
            }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"71",query)


 def test_brands_and_categ_and_behaviours_and_country_us_and_state_and_gender_and_age_and_exclude_dma_and_exclude_brand(self):

    query = "Find users who live in US and visited walmart and restaurants and Golfers and belong to gender male and of age 18-24 and state california and exclude brand target" \
            "and exclude dma- los angeles"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [{
                            "type": "country",
                            "value": "us"
                        }, {
                            "type": "AND",
                            "value": [{
                                "type": "brand",
                                "value": {
                                    "id": 9
                                }
                            }, {
                                "type": "behavior",
                                "value": "go"
                            },
                                {
                                "type": "category",
                                "value": {
                                    "id": "581208"
                                }
                            }
                                ]
                        },
                            {
                                "type": "state",
                                "value": "ca"
                            },
                            {
                                "type" :"NOT",
                                "value" :{"type":"dma","value":803}
                            },

                            {
                                "type":"gender",
                                "value":"m"
                            },

                            {
                                "type": "NOT",
                                "value":{"type":"brand","value":{"id": 10}}

                            },
                            {
                                "type": "age",
                                "value":2
                            }
                        ]
                    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"72",query)

 def test_brands_or_categ_or_behaviours_and_country_us_and_state_and_gender_and_age_and_exclude_dma_and_exclude_brand(self):

    query = "Find users who live in US and visited walmart or restaurants or Golfers and belong to gender male and of age 18-24 and state california and exclude brand target" \
            "and exclude dma- los angeles"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [{
                            "type": "country",
                            "value": "us"
                        }, {
                            "type": "OR",
                            "value": [{
                                "type": "brand",
                                "value": {
                                    "id": 9
                                }
                            }, {
                                "type": "behavior",
                                "value": "go"
                            },
                                {
                                "type": "category",
                                "value": {
                                    "id": "581208"
                                }
                            }
                                ]
                        },
                            {
                                "type": "state",
                                "value": "ca"
                            },
                            {
                                "type" :"NOT",
                                "value" :{"type":"dma","value":803}
                            },

                            {
                                "type":"gender",
                                "value":"m"
                            },

                            {
                                "type": "NOT",
                                "value":{"type":"brand","value":{"id": 10}}

                            },
                            {
                                "type": "age",
                                "value":2
                            }
                        ]
                    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"73",query)

 def test_brands_and_categ_and_behaviours_and_country_us_and_state_and_gender_and_multiple_age_and_exclude_dma_and_exclude_brand(self):

    query = "Find users who live in US and visited walmart and restaurants and Golfers and belong to gender male and of age 18-24 or 25-34 and state california and exclude brand target" \
            "and exclude dma- los angeles"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [{
                            "type": "country",
                            "value": "us"
                        }, {
                            "type": "AND",
                            "value": [{
                                "type": "brand",
                                "value": {
                                    "id": 9
                                }
                            }, {
                                "type": "behavior",
                                "value": "go"
                            },
                                {
                                "type": "category",
                                "value": {
                                    "id": "581208"
                                }
                            }
                                ]
                        },
                            {
                                "type": "state",
                                "value": "ca"
                            },
                            {
                                "type" :"NOT",
                                "value" :{"type":"dma","value":803}
                            },

                            {
                                "type":"gender",
                                "value":"m"
                            },

                            {
                                "type": "NOT",
                                "value":{"type":"brand","value":{"id": 10}}

                            },
                            {
                                "type": "OR",
                                "value":[{"type":"age","value":2},{"type": "age","value": 3}]
                            }
                        ]
                    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"74",query)

 def test_brands_and_categ_and_behaviours_and_country_us_and_state_and_gender_and_multiple_age_and_exclude_dma_and_exclude_brand_and_exclude_behavior(self):

    query = "Find users who live in US and visited walmart and restaurants and Golfers and belong to gender male and of age 18-24 or 25-34 and state california and exclude brand target" \
            "and exclude dma- los angeles and exclude business travellers"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [{
                            "type": "country",
                            "value": "us"
                        }, {
                            "type": "AND",
                            "value": [{
                                "type": "brand",
                                "value": {
                                    "id": 9
                                }
                            }, {
                                "type": "behavior",
                                "value": "go"
                            },
                                {
                                "type": "category",
                                "value": {
                                    "id": "581208"
                                }
                            }
                                ]
                        },
                            {
                                "type": "state",
                                "value": "ca"
                            },
                            {
                                "type" :"NOT",
                                "value" :{"type":"dma","value":803}
                            },

                            {
                                "type":"gender",
                                "value":"m"
                            },

                            {
                                "type":"AND","value":[{ "type": "NOT","value": {"type":"brand","value":{"id": 10}}},
                                                      { "type": "NOT","value": {"type":"behavior","value":"bt"}}]


                            },
                            {
                                "type": "OR",
                                "value":[{"type":"age","value":2},{"type": "age","value": 3}]
                            }
                        ]
                    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"75",query)

 def test_brands_or_categ_or_behaviours_and_country_us_and_state_and_gender_and_multiple_age_and_exclude_dma_and_exclude_brand_and_exclude_behavior(self):

    query = "Find users who live in US and visited walmart or restaurants or Golfers and belong to gender male and of age 18-24 or 25-34 and state california and exclude brand target" \
            "and exclude dma- los angeles and exclude business travellers"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [{
                            "type": "country",
                            "value": "us"
                        }, {
                            "type": "OR",
                            "value": [{
                                "type": "brand",
                                "value": {
                                    "id": 9
                                }
                            }, {
                                "type": "behavior",
                                "value": "go"
                            },
                                {
                                "type": "category",
                                "value": {
                                    "id": "581208"
                                }
                            }
                                ]
                        },
                            {
                                "type": "state",
                                "value": "ca"
                            },
                            {
                                "type" :"NOT",
                                "value" :{"type":"dma","value":803}
                            },

                            {
                                "type":"gender",
                                "value":"m"
                            },

                            {
                                "type":"AND","value":[{ "type": "NOT","value": {"type":"brand","value":{"id": 10}}},
                                                      { "type": "NOT","value": {"type":"behavior","value":"bt"}}]


                            },
                            {
                                "type": "OR",
                                "value":[{"type":"age","value":2},{"type": "age","value": 3}]
                            }
                        ]
                    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"76",query)

 ## Find users who live in US and of segment s1 and of not segment s2 and (seg s3 or seg s4) ##
 def test_users_in_us_and_or_not_and_between_segments(self):

     query = "Find users who lives in country US and of segment DLX Auto powered by Polk: Auto Parts Buyer  (iOS) and not of segment Kantar Shopcom CPG Buyer: Pizza  (Android)" \
             "and of segment Kantar Shopcom IRI CPG Buyer: Juice  (Android) or  DLX Auto powered by Polk: In Market: Used  (iOS)"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
          "OR":{"segment":["202551","214996"]},
          "country":{"direct":["us"]},
          "NOT":{"segment":["330465"]},
          "segment":{"direct":["336555"]}

     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"77",query)

 def test_brands_or_categ_or_behaviours_and_country_us_and_state_and_gender_and_multiple_age_and_exclude_dma_and_exclude_brand_and_exclude_behavior_include_and_exclude_segment(self):

    query = "Find users who live in US and visited walmart or restaurants or Golfers and belong to gender male and of age 18-24 or 25-34 and state california and exclude brand target" \
            "and exclude dma- los angeles and exclude business travellers and include DLX Auto powered by Polk: Auto Parts Buyer  (iOS) and exclude DLX Auto powered by Polk: Auto Service Buyer  (iOS)"
    logger.info("### Usecase:"+str(query)+" ###")

    request = {
                        "type": "AND",
                        "value": [{
                            "type": "country",
                            "value": "us"
                        }, {
                            "type": "OR",
                            "value": [{
                                "type": "brand",
                                "value": {
                                    "id": 9
                                }
                            }, {
                                "type": "behavior",
                                "value": "go"
                            },
                                {
                                "type": "category",
                                "value": {
                                    "id": "581208"
                                }
                            }
                                ]
                        },
                            {
                                "type": "state",
                                "value": "ca"
                            },
                            {
                                "type" :"NOT",
                                "value" :{"type":"dma","value":803}
                            },

                            {
                                "type":"gender",
                                "value":"m"
                            },

                            {
                                "type":"AND","value":[{ "type": "NOT","value": {"type":"brand","value":{"id": 10}}},
                                                      { "type": "NOT","value": {"type":"behavior","value":"bt"}}]


                            },
                            {
                                "type": "OR",
                                "value":[{"type":"age","value":2},{"type": "age","value": 3}]
                            },
                            {
                            "type":"segment",
                            "value":336555
                          },
                            {
                                "type" :"NOT",
                                "value" :{"type":"segment","value":336560}
                            }
                        ]
                    }

    path = API_URL + "/segment_size?query="+str(json.dumps(request))
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: " +json.dumps(request))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))
    count = response.json()['num_audience']
    verify_data_in_db_helper(count,"78",query)

 ## Find users who live in US and are female and are stay at homes ##
 def test_users_in_us_and_stay_at_mom_and_are_female(self):

     query = "Find users who lives in country US and female and are stay at moms"
     logger.info("### Usecase:"+str(query)+" ###")
     request = {
          "country":{"direct":["us"]},
          "behavior":{"direct":["shmom"]},
          "gender":{"direct":["f"]}
     }

     count = segment_size_post("AND",request,db_validation=False)
     verify_data_in_db_helper(count,"79",query)

 ## Find users who dont have a country ##
 def test_users_who_dont_have_country(self):

     query = "Find users who dont have country"
     logger.info("### Usecase:"+str(query)+" ###")

     request1 = {
              "country":{"direct":["us"]},
              "NOT":{"country":["us"]}
               }

     count1 = segment_size_post("OR",request1,db_validation=False)
     logger.info("Total user count: "+str(count1))

     request2 = {"type": "OR", "value": [{"type": "country", "value": "us"}, {"type": "country", "value": "de"}, {"type": "country", "value": "in"}, {"type": "country", "value": "fr"}, {"type": "country", "value": "cn"}, {"type": "country", "value": "gb"}, {"type": "country", "value": "jp"}, {"type": "country", "value": "es"}, {"type": "country", "value": "ca"}, {"type": "country", "value": "it"}, {"type": "country", "value": "au"}, {"type": "country", "value": "mx"}, {"type": "country", "value": "nl"}, {"type": "country", "value": "at"}, {"type": "country", "value": "be"}, {"type": "country", "value": "ch"}, {"type": "country", "value": "dk"}, {"type": "country", "value": "fi"}, {"type": "country", "value": "lu"}, {"type": "country", "value": "no"}, {"type": "country", "value": "se"}, {"type": "country", "value": "nz"}]}
     path = API_URL + "/segment_size?query="+str(json.dumps(request2))
     response = requests.get(path)
     count2 = response.json()['num_audience']
     logger.info("Users of all countries: "+str(count2))
     final_count = int(count1) - int(count2)
     logger.info("Users who dont have country: "+str(final_count))

     verify_data_in_db_helper(final_count,"80",query)



 @classmethod
 def tearDownClass(cls):

     logger.info("#######################################################")
     logger.info("################## Query Results ######################")
     logger.info("#######################################################")
     print t.draw()




if __name__ == '__main__':
    unittest.main()



