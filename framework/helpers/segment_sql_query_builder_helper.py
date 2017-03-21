import json
from collections import defaultdict
import random
from framework.helpers.mysql_helper import *

def token_converter_for_query_builder(input):
    input_string = json.dumps(input)
    new_string = input_string.replace("segment","seg")
    new_string = new_string.replace("brand","b")
    new_string = new_string.replace("age","a")
    new_string = new_string.replace("gender","pg")
    new_string = new_string.replace("income","i")
    new_string = new_string.replace("behavior","bAud")
    new_string = new_string.replace("country","co")
    new_string = new_string.replace("state","st")
    new_string = new_string.replace("zip","z")
    new_string = new_string.replace("dma","d")
    new_string = new_string.replace("category","l")

    input_json = json.loads(new_string)
    return input_json

def token_converter_for_single_token(input):

    new_string = None

    token_map = dict()
    token_map["segment"] = "seg"
    token_map["brand"] = "b"
    token_map["age"] = "a"
    token_map["gender"] = "pg"
    token_map["income"] = "i"
    token_map["behavior"] = "bAud"
    token_map["country"] = "co"
    token_map["state"] = "st"
    token_map["zip"] = "z"
    token_map["dma"] = "d"
    token_map["category"] = "l"

    for key in token_map:
        if input == key:
            new_string = input.replace(key,token_map[key])
    return new_string

def segment_sql_query_builder(main_type, token_map):

    main_query = None
    unum = 1
    if main_type is None:

        if len(token_map) is 1:

            for key in token_map:

                if key != "NOT" and key != "AND" and key != "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key

                        if key2 == "direct":

                            value = value1[key2]
                            for i in value:
                                query = "select count(distinct uid) from userstore where token='"+key1+ "' AND token_value= '"+str(i)+"'"
                                main_query = query

                elif key == "AND":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        values = value1[key2]
                        subquery = "select count(distinct u.uid) from userstore u where "
                        for i,value in enumerate(values):
                            if i > 0:
                                subquery += ' AND '
                            subquery += "u.uid IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        main_query = subquery

                elif key == "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery = "select count(distinct u.uid) from userstore u where "
                        for i, value in enumerate(value_list):
                            if i > 0:
                              subquery += ' OR '
                            subquery += "u.uid IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        main_query = subquery

                elif key == "NOT":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery = "select count(distinct uid) from userstore u where "
                        for i,value in enumerate(value_list):
                            if i > 0:
                                subquery += ' OR '
                            subquery += "u.uid NOT IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        main_query = subquery
    else:

            sub_query_list = []

            for key in token_map:

                if key != "NOT" and key != "AND" and key != "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key

                        if key2 == "direct":

                            value = value1[key2]
                            for i in value:

                                query = "u.uid IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key1+"' AND u{num}.token_value= '"+ \
                                        str(i)+"')"
                                subquery = query.format(num=unum)
                                unum += 1
                            sub_query_list.append("("+subquery+ ")")

                elif key == "AND":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        values = value1[key2]
                        subquery = ""
                        for i,value in enumerate(values):
                            if i > 0:
                                subquery += ' AND '
                            subquery += "u.uid IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        sub_query_list.append("("+subquery+ ")")

                elif key == "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery= ""
                        for i, value in enumerate(value_list):
                            if i > 0:
                              subquery += ' OR '
                            subquery += "u.uid IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                    sub_query_list.append("("+subquery+ ")")

                elif key == "NOT":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery = ""
                        for i,value in enumerate(value_list):
                            if i > 0:
                                subquery += ' OR '
                            subquery += "u.uid NOT IN (select u{num}.uid from userstore u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        sub_query_list.append("( "+subquery+ ")")

            full_query = ""
            for i,value in enumerate(sub_query_list):
                if i > 0:
                    full_query += ' ' + main_type + ' '
                full_query += value
            main_query = "select count(distinct u.uid) from userstore u where ("+full_query+")"

    return main_query



def user_count_by_gender(gender_type):

    cnx = mysql_connect('test_cab')

    pg_query = "select distinct uid as uid, token_value from userstore where token='pg'"
    data = get_all_result(cnx, pg_query)

    users_count = {'m': 0, 'f': 0}
    for row in data:
        if row['token_value'] in users_count:
            users_count[row['token_value']] += 1

    gender_query = ("select distinct uid as uid, token_value from userstore where token='g' "
                    "and uid not in (select uid from userstore where token= 'pg')")
    data = get_all_result(cnx, gender_query)

    cur_uid = ''
    for row in data:
        uid = row['uid']
        gender = row['token_value']
        if uid != cur_uid:
            if cur_uid != '':

                # find max gender and update user count dict.
                main_gender = 'f'
                if temp_count['m'] > temp_count['f']:
                    main_gender = 'm'
                elif temp_count['m'] < temp_count['f']:
                    main_gender = 'f'
                else:
                    main_gender = random.choice(temp_count.keys())
                users_count[main_gender] += 1

            # count for new uid
            temp_count = {'m': 0, 'f': 0}
            cur_uid = uid
            temp_count[gender] += 1
        else:
            temp_count[gender] += 1

    cnx.close()

    return users_count[gender_type]

def user_count_by_gender_logic2(gender_type):

    cnx = mysql_connect('test_cab')

    pg_query_by_gender = "select count(distinct uid) from userstore where token='pg' and token_value='"+gender_type+"'"
    data = get_result(cnx, pg_query_by_gender)
    pg_query_count_by_gender = (data['count(distinct uid)'])
    cnx.close()

    cnx = mysql_connect('test_cab')
    gender_query = ("select uid, token_value from userstore where token='g' "
                    "and uid not in (select uid from userstore where token= 'pg')")
    data = get_all_result(cnx, gender_query)
    uid_gender_map =dict()

    for row in data:
        if row['uid'] not in uid_gender_map.keys():
             uid_gender_map[row['uid']] = []
             uid_gender_map[row['uid']].append(row['token_value'])
        else:
            uid_gender_map[row['uid']].append(row['token_value'])
    cnx.close()

    gender_map_final = dict()

    for key in uid_gender_map:
        pg =''
        value_list = uid_gender_map[key]
        m_count= 0
        f_count= 0
        for i in value_list:
            if i == 'm':
                m_count +=1
            else:
                f_count +=1

        if m_count > f_count:
         pg='m'
        elif f_count > m_count:
         pg='f'
        else:
         g =['m','f']
         pg = random.choice(g)

        gender_map_final[key] = pg

    sub_gen_count =0

    for key in gender_map_final:
        v = gender_map_final[key]
        if v == gender_type:
            sub_gen_count +=1


    return sub_gen_count+int(pg_query_count_by_gender)


def user_count_age(current_year, age_enum):

    age_map = {

        0: 13,
        1: 18,
        2: 25,
        3: 35,
        4: 45,
        5: 55,
        6: 65,
        7: 999
    }

    cnx = mysql_connect('test_cab')

    actual_query = "select distinct uid as uid, token_value from userstore where token='a' "

    data = get_all_result(cnx, actual_query)

    cur_uid = ''
    users_count = defaultdict(int)
    for row in data:
        uid = row['uid']
        if row['token_value'] == '':
            continue
        age = current_year - int(row['token_value'])
        if uid != cur_uid:
            if cur_uid != '':
                best_age = 0
                best_count = 0

                for k in sorted(temp_count,key=temp_count.get, reverse=True):
                    if temp_count[k] > best_count:
                        best_count = temp_count[k]
                        best_age = k

                # If the max frequency is 1 implies no majority can be found.
                if best_count == 1:
                    best_age = random.choice(temp_count.keys())
                users_count[cur_uid] = best_age

            # count for new uid
            temp_count = defaultdict(int)
            cur_uid = uid
            temp_count[age] += 1
        else:
            temp_count[age] += 1

    cnx.close()

    age_limit = 0
    if age_enum in age_map:
        age_limit = age_map[age_enum]

    results = []

    # Filter uids which match the enum condition
    for uid in users_count:

        if age_limit is 18:
         if (users_count[uid] >= 13) and (users_count[uid] <=17) :
            results.append(uid)
        if age_limit is 25:
            if (users_count[uid] >= 18) and (users_count[uid] <=24) :
             results.append(uid)
        if age_limit is 35:
            if (users_count[uid] >= 25) and (users_count[uid] <=34) :
             results.append(uid)
        if age_limit is 45:
            if (users_count[uid] >= 35) and (users_count[uid] <=44) :
             results.append(uid)
        if age_limit is 55:
            if (users_count[uid] >= 45) and (users_count[uid] <=54) :
             results.append(uid)
        if age_limit is 65:
            if (users_count[uid] >= 55) and (users_count[uid] <=64) :
             results.append(uid)
        if age_limit is 999:
            if users_count[uid] >= 65 :
             results.append(uid)

    return len(results)











