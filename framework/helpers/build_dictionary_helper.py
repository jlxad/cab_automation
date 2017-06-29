import dill
import random
import datetime
import os
from config import *
from framework.helpers.mysql_helper import *

now = datetime.datetime.now()
cur_year = now.year
data = read_data_from_config_json("config.json")
state_list = data['states']

if len(sys.argv) > 2:
    fileDir = data['jenkins_qa_host']
else:
    fileDir = os.path.dirname(os.path.realpath('__file__'))


def create_dictionary_from_file(file_path):
    user_attributes_list = data['user_attributes_map_list']
    user_attributes_location_in_file = data['attributes_positions_in_data_file']
    age_map = user_attributes_list['age_map']
    for ele in age_map:
        data['user_attributes_map_list']['age_map'][ele] = set()

    with open(file_path, 'r') as document:

        for line in document:

            line = line.split("\t")

            if not line:
                continue

            # Brand Map
            user_attributes_list['brand_map'] = construct_brand_category_dict(line, user_attributes_list['brand_map'],
                                                                              user_attributes_location_in_file['brand'])

            # Category Map
            user_attributes_list['category_map'] = construct_brand_category_dict(line,
                                                                                 user_attributes_list['category_map'],
                                                                                 user_attributes_location_in_file[
                                                                                     'category'])

            # Behavioural Audiences Map
            user_attributes_list['behaviour_audience_map'] = construct_behaviour_third_party_audience_map(line,
                                                                                                          user_attributes_list[
                                                                                                              'behaviour_audience_map'],
                                                                                                          user_attributes_location_in_file[
                                                                                                              'behavioural_audience'])

            # Third party audiences or segments Map
            user_attributes_list['custom_audience_map'] = construct_behaviour_third_party_audience_map(line,
                                                                                                       user_attributes_list[
                                                                                                           'custom_audience_map'],
                                                                                                       user_attributes_location_in_file[
                                                                                                           'custom_audience'])
            # Country
            user_attributes_list['country_map'] = construct_country_state_dma_map(line,
                                                                                  user_attributes_list['country_map'],
                                                                                  user_attributes_location_in_file[
                                                                                      'country'])

            # State
            user_attributes_list['state_map'] = construct_country_state_dma_map(line, user_attributes_list['state_map'],
                                                                                user_attributes_location_in_file[
                                                                                    'state'])

            # Dma
            user_attributes_list['dma_map'] = construct_country_state_dma_map(line, user_attributes_list['dma_map'],
                                                                              user_attributes_location_in_file['dma'])

            # Gender Map
            user_attributes_list['gender_map'] = construct_gender_map(line, user_attributes_list['gender_map'])

            # Age
            user_attributes_list['age_map'] = construct_age_map(line, user_attributes_list['age_map'])

    dump_locations_map = data['dump_location']

    # Serialization process. Converting the data in the raw data file to dictionaries
    for element in dump_locations_map:
        dill.dump(user_attributes_list[element],
                  open(fileDir + "/resources/" + dump_locations_map[element] + ".txt", "w"), -1)


# data_row is a record or a line in the text file. Creating a brand and category dictionary by parsing each
# column of data from the raw data file
# location_in_file represents the column number in which brand or category data is present
def construct_brand_category_dict(data_row, user_attribute_map, location_in_file):
    freq_numbers_list = data['frequency_numbers']
    user_attributes_location_in_file = data['attributes_positions_in_data_file']

    if data_row[location_in_file] != '':

        user_attribute_values_list = data_row[location_in_file].split("|")

        for ele in user_attribute_values_list:

            if ele != '':
                ele_list = ele.split(",")
                e_str = ele_list[0] + "," + ele_list[1]

                frequency_dict = {}

                for frequency in freq_numbers_list:
                    frequency_dict[frequency] = set()

                if e_str not in user_attribute_map:
                    if int(ele_list[2]) >= 10:
                        frequency_dict[10].add(data_row[user_attributes_location_in_file['user_id']])
                        frequency_dict[5].add(data_row[user_attributes_location_in_file['user_id']])
                        frequency_dict[1].add(data_row[user_attributes_location_in_file['user_id']])

                    elif int(ele_list[2]) >= 5:
                        frequency_dict[5].add(data_row[user_attributes_location_in_file['user_id']])
                        frequency_dict[1].add(data_row[user_attributes_location_in_file['user_id']])

                    elif int(ele_list[2]) >= 1:
                        frequency_dict[1].add(data_row[user_attributes_location_in_file['user_id']])

                    user_attribute_map[e_str] = frequency_dict
                else:
                    range1 = False
                    range5 = False
                    range10 = False
                    if int(ele_list[2]) >= 1:
                        range1 = True
                    if int(ele_list[2]) >= 5:
                        range5 = True
                    if int(ele_list[2]) >= 10:
                        range10 = True

                    if range10 is True:
                        user_attribute_map[e_str][10].add(data_row[user_attributes_location_in_file['user_id']])
                        user_attribute_map[e_str][5].add(data_row[user_attributes_location_in_file['user_id']])
                        user_attribute_map[e_str][1].add(data_row[user_attributes_location_in_file['user_id']])
                    if range1 is True:
                        user_attribute_map[e_str][1].add(data_row[user_attributes_location_in_file['user_id']])
                    if range5 is True:
                        user_attribute_map[e_str][5].add(data_row[user_attributes_location_in_file['user_id']])
                        user_attribute_map[e_str][1].add(data_row[user_attributes_location_in_file['user_id']])

    return user_attribute_map


# data_row is a record or a line in the text file. Creating a behavioural audience and third party audience
# dictionary by parsing each column of data from the raw data file
# location_in_file represents the column number in which behavioural audience or custom audience data is present
def construct_behaviour_third_party_audience_map(data_row, user_attribute_map, location_in_file):
    user_attributes_location_in_file = data['attributes_positions_in_data_file']

    if data_row[location_in_file] != '':
        audience_list = data_row[location_in_file].split("|")
        for ele in audience_list:
            audience_set = set()
            if ele not in user_attribute_map:
                audience_set.add(data_row[user_attributes_location_in_file['user_id']])
                user_attribute_map[ele] = audience_set
            else:
                user_attribute_map[ele].add(data_row[user_attributes_location_in_file['user_id']])
    return user_attribute_map


# data_row is a record or a line in the text file. Creating country,state and dma
# dictionary by parsing each column of data from the raw data file
# location_in_file represents the column number in which country,state or dma data is present
def construct_country_state_dma_map(data_row, user_attribute_map, location_in_file):
    user_attributes_location_in_file = data['attributes_positions_in_data_file']

    # Country
    if location_in_file is user_attributes_location_in_file['country'] and \
                    data_row[user_attributes_location_in_file['state']] != '':
        if data_row[user_attributes_location_in_file['state']] in state_list:
            if "us" in user_attribute_map:
                user_attribute_map['us'].add(data_row[user_attributes_location_in_file['user_id']])
            else:
                user_id_list = set()
                user_id_list.add(data_row[user_attributes_location_in_file['user_id']])
                user_attribute_map['us'] = user_id_list
        else:
            if data_row[user_attributes_location_in_file['country']] != '':
                country_list = data_row[user_attributes_location_in_file['country']].split("|")
                for ele in country_list:
                    if ele not in user_attribute_map:
                        user_ids = set()
                        user_ids.add(data_row[user_attributes_location_in_file]['user_id'])
                        user_attribute_map[ele] = user_ids
                    else:
                        user_attribute_map[ele].add(data_row[user_attributes_location_in_file['user_id']])
    else:

        if data_row[user_attributes_location_in_file['country']] != '':
            country_list = data_row[user_attributes_location_in_file['country']].split("|")
            for ele in country_list:
                if ele not in user_attribute_map:
                    user_ids = set()
                    user_ids.add(data_row[user_attributes_location_in_file['user_id']])
                    user_attribute_map[ele] = user_ids
                else:
                    user_attribute_map[ele].add(data_row[user_attributes_location_in_file['user_id']])
    # State
    if location_in_file is user_attributes_location_in_file['state'] and \
                    data_row[user_attributes_location_in_file['state']] != '':
        if data_row[user_attributes_location_in_file['state']] not in user_attribute_map:
            user_ids = set()
            user_ids.add(data_row[user_attributes_location_in_file['user_id']])
            user_attribute_map[data_row[user_attributes_location_in_file['state']]] = user_ids
        else:
            user_attribute_map[data_row[user_attributes_location_in_file['state']]].add(
                data_row[user_attributes_location_in_file['user_id']])

    # Dma
    if location_in_file is user_attributes_location_in_file['dma'] and \
                    data_row[user_attributes_location_in_file['dma']] != '':
        if data_row[user_attributes_location_in_file['dma']] not in user_attribute_map:
            user_ids = set()
            user_ids.add(data_row[user_attributes_location_in_file['user_id']])
            user_attribute_map[data_row[user_attributes_location_in_file['dma']]] = user_ids
        else:
            user_attribute_map[data_row[user_attributes_location_in_file['dma']]].add(
                data_row[user_attributes_location_in_file['user_id']])

    return user_attribute_map


# data_row is a record or a line in the text file. Creating a gender dictionary by parsing each
# column of data from the raw data file
def construct_gender_map(data_row, user_attribute_map):
    user_attributes_location_in_file = data['attributes_positions_in_data_file']

    if data_row[user_attributes_location_in_file['predicted_gender']] != '':
        if data_row[user_attributes_location_in_file['predicted_gender']] not in user_attribute_map:
            user_ids = set()
            user_ids.add(data_row[user_attributes_location_in_file['user_id']])
            user_attribute_map[data_row[user_attributes_location_in_file['predicted_gender']]] = user_ids
        else:

            user_attribute_map[data_row[user_attributes_location_in_file['predicted_gender']]].add(
                data_row[user_attributes_location_in_file['user_id']])

    # Gender Value from Gender column
    elif data_row[user_attributes_location_in_file['gender']] != '':
        gender_list = data_row[user_attributes_location_in_file['gender']].split("|")
        gen_map = {"m": 0, "f": 0}

        for ele in gender_list:
            if ele != '':
                gen_map[ele] += 1

        if int(gen_map['m']) > int(gen_map['f']):
            pg = 'm'
        elif int(gen_map['f']) > int(gen_map['m']):
            pg = 'f'
        else:
            g = ['m', 'f']
            pg = random.choice(g)

        if pg not in user_attribute_map:
            user_ids = set()
            user_ids.add(data_row[user_attributes_location_in_file['user_id']])
            user_attribute_map[pg] = user_ids
        else:
            user_attribute_map[pg].add(data_row[user_attributes_location_in_file['user_id']])

    if data_row[user_attributes_location_in_file['gender']] == '' and \
                    data_row[user_attributes_location_in_file['predicted_gender']] == '':

        if "unknown" not in user_attribute_map:
            user_ids = set()
            user_ids.add(data_row[user_attributes_location_in_file['user_id']])
            user_attribute_map['unknown'] = user_ids
        else:
            user_attribute_map['unknown'].add(data_row[user_attributes_location_in_file['user_id']])

    return user_attribute_map


# data_row is a record or a line in the text file. Creating an age dictionary by parsing each
# column of data from the raw data file
def construct_age_map(data_row, user_attribute_map):
    user_attributes_location_in_file = data['attributes_positions_in_data_file']

    if data_row[user_attributes_location_in_file['age']] != '':
        age_list = data_row[user_attributes_location_in_file['age']].split("|")
        age_dict = dict()
        for age in age_list:
            converted_age = int(cur_year) - int(age)
            if converted_age not in age_dict:
                age_dict[converted_age] = 1
            else:
                val = age_dict[converted_age]
                age_dict[converted_age] = val + 1

        maximum_fre = max(age_dict, key=age_dict.get)
        if age_dict[maximum_fre] is 1 and len(age_dict) is not 1:
            predicted_age = random.choice(age_dict.keys())
        else:
            predicted_age = maximum_fre
        if (predicted_age >= 13) and (predicted_age <= 17):
            user_attribute_map['1'].add(data_row[user_attributes_location_in_file['user_id']])
        if (predicted_age >= 18) and (predicted_age <= 24):
            user_attribute_map['2'].add(data_row[user_attributes_location_in_file['user_id']])
        if (predicted_age >= 25) and (predicted_age <= 34):
            user_attribute_map['3'].add(data_row[user_attributes_location_in_file['user_id']])
        if (predicted_age >= 35) and (predicted_age <= 44):
            user_attribute_map['4'].add(data_row[user_attributes_location_in_file['user_id']])
        if (predicted_age >= 45) and (predicted_age <= 54):
            user_attribute_map['5'].add(data_row[user_attributes_location_in_file['user_id']])
        if (predicted_age >= 55) and (predicted_age <= 64):
            user_attribute_map['6'].add(data_row[user_attributes_location_in_file['user_id']])
        if predicted_age >= 65:
            user_attribute_map['7'].add(data_row[user_attributes_location_in_file['user_id']])
    else:
        user_attribute_map['0'].add(data_row[user_attributes_location_in_file['user_id']])

    return user_attribute_map
