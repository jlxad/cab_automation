import dill
import datetime as dt
import pandas as pd
import logging
import string
from framework.helpers.build_dictionary_helper import *
logger = logging.getLogger("cab.helpers.dictionary_query_builder")

create_dictionary_from_file('/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/dump.txt')
country_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/country.txt"))
state_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/state.txt"))
dma_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/dma.txt"))
brand_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/brand.txt"))
category_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/category.txt"))
age_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/age.txt"))
gender_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/gender.txt"))
baud_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/baud.txt"))
customaud_map = dill.load(open("/Users/sakthigurumaharaj/PycharmProjects/cab_v2_automation/resources/customaud.txt"))

map_token = {

        "country": country_map,
        "brand": brand_map,
        "category": category_map,
        "state": state_map,
        "dma": dma_map,
        "age": age_map,
        "gender": gender_map,
        "behavior": baud_map,
        "segment": customaud_map
    }

def get_result_from_dictionary_single_row_logical_operations(main_type, request_map):

    token_map = request_map

    if main_type is None and len(request_map) is 1:

        for key in token_map:

            key1 = key
            value1 = token_map[key1]

            for key2 in value1:

                if key2 != "direct" and key2 == "brand":

                    value_list = value1[key2]
                    combined_set = []

                    for val in value_list:
                        val_split = val.split("|")
                        id = val_split[0]
                        minfreq = val_split[1]
                        duration = val_split[2]
                        timeofday = val_split[3]
                        dayofweek = val_split[4]
                        pattern = get_pattern(id,duration,timeofday,dayofweek)

                        if pattern in map_token[key2] and duration != "6m":

                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                          set1 = brand_map[pattern][int(minfreq)]
                          combined_set.append(set1)

                        elif pattern in map_token[key2] and duration == "6m":

                          last_but_one_qrtr_pattern = pattern.replace("_"+str(get_last_quarter()),"_"+str(get_last_but_one_quarter(get_last_quarter())))
                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq)+"|"+str(last_but_one_qrtr_pattern)+","+str(minfreq))
                          brands_uids_union = brand_map[pattern][int(minfreq)] | brand_map[last_but_one_qrtr_pattern][int(minfreq)]
                          set1 = brands_uids_union
                          combined_set.append(set1)

                        else:
                         logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                         set1 = set()
                         combined_set.append(set1)

                    if key1 == "AND":
                        big_intersection = set.intersection(*combined_set)
                        return len(big_intersection)

                    if key1 == "OR":
                        big_union = set.union(*combined_set)
                        return len(big_union)

                if key2 == "direct" and key1 == "category":
                    value_list = value1[key2]
                    for val in value_list:
                        val_split = val.split("|")
                        id = val_split[0]
                        minfreq = val_split[1]
                        duration = val_split[2]
                        timeofday = val_split[3]
                        dayofweek = val_split[4]
                        pattern = get_pattern(id,duration,timeofday,dayofweek)

                        if pattern in map_token[key2] and duration != "6m":

                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                          return len(category_map[pattern][int(minfreq)])

                        elif pattern in map_token[key2] and duration == "6m":

                          last_but_one_qrtr_pattern = pattern.replace("_"+str(get_last_quarter()),"_"+str(get_last_but_one_quarter(get_last_quarter())))
                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq)+"|"+str(last_but_one_qrtr_pattern)+","+str(minfreq))
                          categ_uids_union = category_map[pattern][int(minfreq)] | category_map[last_but_one_qrtr_pattern][int(minfreq)]
                          return len(categ_uids_union)

                        else:
                         logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                         return 0



def get_result_from_dictionary_single_row(main_type, request_map):

    token_map = request_map

    if main_type is None and len(request_map) is 1:

        for key in token_map:

            key1 = key
            value1 = token_map[key1]

            for key2 in value1:

                if key2 == "direct" and key1 == "brand":
                    value_list = value1[key2]
                    for val in value_list:
                        val_split = val.split("|")
                        id=val_split[0]
                        minfreq = val_split[1]
                        duration = val_split[2]
                        timeofday = val_split[3]
                        dayofweek = val_split[4]
                        pattern = get_pattern(id,duration,timeofday,dayofweek)
                        if pattern in map_token[key1] and duration != "6m":
                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                          return len(brand_map[pattern][int(minfreq)])

                        elif pattern in map_token[key1] and duration == "6m":
                          last_but_one_qrtr_pattern = pattern.replace("_"+str(get_last_quarter()),"_"+str(get_last_but_one_quarter(get_last_quarter())))
                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq)+"|"+str(last_but_one_qrtr_pattern)+","+str(minfreq))
                          brands_uids_union = brand_map[pattern][int(minfreq)] | brand_map[last_but_one_qrtr_pattern][int(minfreq)]
                          return len(brands_uids_union)

                        else:
                         logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                         return 0

                if key2 == "direct" and key1 == "category":
                    value_list = value1[key2]
                    for val in value_list:
                        val_split = val.split("|")
                        id=val_split[0]
                        minfreq = val_split[1]
                        duration = val_split[2]
                        timeofday = val_split[3]
                        dayofweek = val_split[4]
                        pattern = get_pattern(id, duration, timeofday,dayofweek)

                        if pattern in map_token[key1] and duration != "6m":

                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                          return len(category_map[pattern][int(minfreq)])

                        elif pattern in map_token[key1] and duration == "6m":

                          last_but_one_qrtr_pattern = pattern.replace("_"+str(get_last_quarter()),"_"+str(get_last_but_one_quarter(get_last_quarter())))
                          logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq)+"|"+str(last_but_one_qrtr_pattern)+","+str(minfreq))
                          categ_uids_union = category_map[pattern][int(minfreq)] | category_map[last_but_one_qrtr_pattern][int(minfreq)]
                          return len(categ_uids_union)

                        else:
                         logger.info("Dictionary Query- "+str(pattern)+","+str(minfreq))
                         return 0

                if key2 == "direct" and key1 == "country":
                     value_list = value1[key2]
                     for val in value_list:
                      country = val
                     return len(country_map[country])

                if key2 == "direct" and key1 == "state":
                    value_list = value1[key2]
                    for val in value_list:
                     state = val
                    return len(state_map[state])

                if key2 == "direct" and key1 == "dma":
                    value_list = value1[key2]
                    for val in value_list:
                     dma = val
                    return len(dma_map[dma])

                if key2 == "direct" and key1 == "age":
                    value_list = value1[key2]
                    for val in value_list:
                     age = val
                    return len(age_map[age])

                if key2 == "direct" and key1 == "gender":
                    value_list = value1[key2]
                    for val in value_list:
                     gender = val
                    return len(gender_map[gender])

                if key2 == "direct" and key1 == "behavior":
                    value_list = value1[key2]
                    for val in value_list:
                     behavior = val
                    return len(baud_map[behavior])

                if key2 == "direct" and key1 == "segment":
                    value_list = value1[key2]
                    for val in value_list:
                     segment = val
                    return len(customaud_map[segment])


def get_pattern(id,duration,timeofday,dayofweek):

    last_quarter = 0
    last_week = 0
    last_month = 0
    last_but_one_quarter = 0

    now = dt.datetime(2017,2,17)
    this_month = now.month
    current_week = dt.datetime(2017,2,17).isocalendar()[1]
    quarter = pd.Timestamp(dt.datetime(2017,2,17)).quarter
    last_two_qrtr = []

    if this_month is 1:
        last_month = 12
    else:
        last_month = this_month-1

    if quarter is 1:
        last_quarter = 4
    else:
        last_quarter = quarter-1

    if last_quarter is 1:
        last_but_one_quarter = 4
    else:
        last_but_one_quarter = last_quarter-1

    if current_week is 1:
        last_week = 52
    else:
        last_week = current_week-1

    last_two_qrtr.append(last_quarter)
    last_two_qrtr.append(last_but_one_quarter)

    duration_map = {
        "1m": ["m",str(last_month)],
        "1w": ["w",str(last_week)],
        "1y": ["yr","1"],
        "1q": ["qrtr",str(last_quarter)],
        "6m": ["qrtr",str(last_quarter)]
    }

    day_of_week_map = {
        "1": ["wkdy","1"],
        "2": ["wknd","1"],
        "3": ["dow","6"],
        "4": ["dow","7"]
    }

    time_of_day_map = {
        "1": ["tod", "1"],
        "2": ["tod", "2"],
        "3": ["tod", "3"],
        "4": ["tod", "4"]

    }

    pattern = ''
    final_pattern = ''

    if duration != 'None' and timeofday == 'None' and dayofweek == 'None':
        pattern = duration_map[duration][0]+"_"+str(duration_map[duration][1])

    if duration != 'None' and timeofday != 'None' and dayofweek == 'None':
        pattern = duration_map[duration][0]+":"+time_of_day_map[timeofday][0]+"_"+str(duration_map[duration][1])+":"\
                +str(time_of_day_map[timeofday][1])

    if duration != 'None' and timeofday == 'None' and dayofweek != 'None':
         pattern = duration_map[duration][0]+":"+day_of_week_map[dayofweek][0]+"_"+str(duration_map[duration][1])+":"\
                +str(day_of_week_map[dayofweek][1])

    if duration != 'None' and timeofday != 'None' and dayofweek != 'None':
         pattern = duration_map[duration][0]+":"+day_of_week_map[dayofweek][0]+":"+time_of_day_map[timeofday][0]+"_"+str(duration_map[duration][1])+":"\
                +str(day_of_week_map[dayofweek][1])+":"+str(time_of_day_map[timeofday][1])

    final_pattern = id+","+pattern
    return final_pattern


def get_last_quarter():

    quarter = pd.Timestamp(dt.datetime(2017,2,17)).quarter
    if quarter is 1:
       return 4
    else:
        return quarter-1

def get_last_but_one_quarter(last_quarter):

    if last_quarter is 1:
        return 4
    else:
        return last_quarter-1


