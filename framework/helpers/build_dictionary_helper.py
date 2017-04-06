import dill
import random
import datetime
import os
import sys

now = datetime.datetime.now()

if len(sys.argv) > 2:
    fileDir = "/media/ephemeral0/jenkins/workspace/CAB_Functional_Tests/cab_automation"
else:
    fileDir = os.path.dirname(os.path.realpath('__file__'))

cur_year =now.year

state_list1 = ['ak','al','ar','az','ca','co','ct','dc','de','fl','ga','ia','id','il','in','ks','ky','la','ma','md',
              'me','mi','mn','mo','ms','mt','nc','nd','ne','nh','nj','nm','nv','ny','oh','ok','or','pa','ri','sc',
              'sd','tn','tx','ut','va','vt','wa','wi','wv','wy','hi']

state_list = ['pa', 'az', 'fl', 'la', 'mt', 'gu', 'nm', 'ak', 'nc', 'or', 'vt', 'ms', 'ar', 'il', 'mo', 'in', 'hi', 'wy',
  'ut', 'mi', 'ks', 'md', 'vi', 'ga', 'dc', 'mn', 'wi', 'ne', 'oh', 'ct', 'nv', 'pr', 'ok', 'al', 'ca', 'co', 'de', 'nd',
  'wv', 'ky', 'wa', 'me', 'ri', 'sd', 'tn', 'va', 'nh', 'ia', 'sc', 'ny', 'ma', 'id', 'nj', 'tx']

def create_dictionary_from_file(file_path):

    brand_map = dict()
    category_map = dict()
    country_map = dict()
    behav_aud_map = dict()
    custom_aud_map = dict()
    state_map = dict()
    dma_map = dict()
    gender_map = dict()
    age_map = {"0":set(),"1": set(),"2": set(),"3": set(),"4": set(),"5": set(),"6": set(),"7": set()}

    with open(file_path, 'r') as document:
            for line in document:
                line = line.split("\t")
                if not line:
                    continue
                # Brand
                if line[1] != '':
                    brand_list = line[1].split("|")
                    for ele in brand_list:
                        if ele != '':
                            ele_list = ele.split(",")
                            e_str = ele_list[0]+","+ele_list[1]
                            l1 = set()
                            l2 = set()
                            l3 = set()
                            d1 = {1: l1, 5: l2, 10: l3}
                            if e_str not in brand_map:
                                if int(ele_list[2]) >= 10:
                                    d1[10].add(line[0])
                                    d1[5].add(line[0])
                                    d1[1].add(line[0])

                                elif int(ele_list[2]) >= 5:
                                    d1[5].add(line[0])
                                    d1[1].add(line[0])

                                elif int(ele_list[2]) >= 1:
                                    d1[1].add(line[0])

                                brand_map[e_str]=d1
                            else:
                                range1 = False
                                range5 = False
                                range10 = False
                                if int(ele_list[2]) >= 1:
                                    range1=True
                                if int(ele_list[2]) >= 5:
                                    range5=True
                                if int(ele_list[2]) >= 10:
                                    range10=True

                                if range10 is True:
                                    brand_map[e_str][10].add(line[0])
                                    brand_map[e_str][5].add(line[0])
                                    brand_map[e_str][1].add(line[0])
                                if range1 is True:
                                    brand_map[e_str][1].add(line[0])
                                if range5 is True:
                                    brand_map[e_str][5].add(line[0])
                                    brand_map[e_str][1].add(line[0])

                # Category
                if line[2] != '':
                  categ_list = line[2].split("|")
                  for ele in categ_list:
                        if ele != '':
                            ele_list = ele.split(",")
                            e_str = ele_list[0]+","+ele_list[1]
                            l1 = set()
                            l2 = set()
                            l3 = set()
                            d1 = {1: l1, 5: l2, 10: l3}
                            if e_str not in category_map:

                                if int(ele_list[2]) >= 10:
                                    d1[10].add(line[0])
                                    d1[5].add(line[0])
                                    d1[1].add(line[0])

                                elif int(ele_list[2]) >= 5:
                                    d1[5].add(line[0])
                                    d1[1].add(line[0])

                                elif int(ele_list[2]) >= 1:
                                    d1[1].add(line[0])

                                category_map[e_str] = d1
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
                                    category_map[e_str][10].add(line[0])
                                    category_map[e_str][5].add(line[0])
                                    category_map[e_str][1].add(line[0])
                                if range1 is True:
                                    category_map[e_str][1].add(line[0])
                                if range5 is True:
                                    category_map[e_str][5].add(line[0])
                                    category_map[e_str][1].add(line[0])

                # Age
                if line[3] != '':
                    age_list = line[3].split("|")
                    age_dict=dict()
                    for age in age_list:
                        converted_age = int(cur_year)-int(age)
                        if converted_age not in age_dict:
                            age_dict[converted_age]=1
                        else:
                           val= age_dict[converted_age]
                           age_dict[converted_age] = val+1

                    maximum_fre = max(age_dict, key=age_dict.get)
                    if age_dict[maximum_fre] is 1 and len(age_dict) is not 1:
                        predicted_age= random.choice(age_dict.keys())
                        # predicted_age = max(age_dict.keys())
                    else:
                        predicted_age = maximum_fre
                    if (predicted_age >= 13) and (predicted_age <=17):
                     age_map['1'].add(line[0])
                    if (predicted_age >= 18) and (predicted_age <=24):
                     age_map['2'].add(line[0])
                    if (predicted_age >= 25) and (predicted_age <=34):
                     age_map['3'].add(line[0])
                    if (predicted_age >= 35) and (predicted_age <=44):
                     age_map['4'].add(line[0])
                    if (predicted_age >= 45) and (predicted_age <=54):
                     age_map['5'].add(line[0])
                    if (predicted_age >= 55) and (predicted_age <=64):
                     age_map['6'].add(line[0])
                    if predicted_age >= 65:
                     age_map['7'].add(line[0])
                else:
                    age_map['0'].add(line[0])

                # Behavioural Audiences
                if line[9] != '':
                    behav_aud_list = line[9].split("|")
                    for ele in behav_aud_list:
                        list_aud = set()
                        if ele not in behav_aud_map:
                            list_aud.add(line[0])
                            behav_aud_map[ele] = list_aud
                        else:
                            behav_aud_map[ele].add(line[0])

                # Third party audiences or segments
                if line[11] != '':
                    custom_list = line[11].split("|")
                    for ele in custom_list:
                        list_caud = set()
                        if ele not in custom_aud_map:
                            list_caud.add(line[0])
                            custom_aud_map[ele] = list_caud
                        else:
                            custom_aud_map[ele].add(line[0])

                # Country
                if line[14] != '':
                    if line[14] in state_list:
                        if "us" in country_map:
                            country_map['us'].add(line[0])
                        else:
                            list2 = set()
                            list2.add(line[0])
                            country_map['us'] = list2
                    else:
                        if line[5] != '':
                            country_list = line[5].split("|")
                            for ele in country_list:
                                if ele not in country_map:
                                    list_c = set()
                                    list_c.add(line[0])
                                    country_map[ele] = list_c
                                else:
                                    country_map[ele].add(line[0])
                else:
                 if line[5] != '':
                    country_list = line[5].split("|")
                    for ele in country_list:
                        if ele not in country_map:
                            list_c = set()
                            list_c.add(line[0])
                            country_map[ele] = list_c
                        else:
                            country_map[ele].add(line[0])
                # State
                if line[14] != '':
                    if line[14] not in state_map:
                        list1=set()
                        list1.add(line[0])
                        state_map[line[14]] = list1
                    else:
                        state_map[line[14]].add(line[0])

                # Dma
                if line[15] != '':
                    if line[15] not in dma_map:
                        list1= set()
                        list1.add(line[0])
                        dma_map[line[15]] = list1
                    else:
                        dma_map[line[15]].add(line[0])

                #Gender
                #Gender value from Predicted Gender column
                if line[7] != '':
                    if line[7] not in gender_map:
                        list1 = set()
                        list1.add(line[0])
                        gender_map[line[7]] = list1
                    else:

                        gender_map[line[7]].add(line[0])

                # Gender Value from Gender column
                elif line[4] != '':
                    pg = None
                    gender_list = line[4].split("|")
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
                    if pg not in gender_map:
                        list1 = set()
                        list1.add(line[0])
                        gender_map[pg] = list1
                    else:
                        gender_map[pg].add(line[0])

                if line[7] == '' and line[4] == '':

                    if "unknown" not in gender_map:
                        list1 = set()
                        list1.add(line[0])
                        gender_map['unknown'] = list1
                    else:
                        gender_map['unknown'].add(line[0])

    # serialize the brand map
    dill.dump(brand_map,open(fileDir+"/resources/brand.txt","w"),-1)

    # serialize the category map
    dill.dump(category_map,open(fileDir+"/resources/category.txt","w"),-1)

    # serialize the country map
    dill.dump(country_map,open(fileDir+"/resources/country.txt","w"),-1)

    # serialize the behavioural audience map
    dill.dump(behav_aud_map,open(fileDir+"/resources/baud.txt","w"),-1)

    # serialize the custom audience map
    dill.dump(custom_aud_map,open(fileDir+"/resources/customaud.txt","w"),-1)

    # serialize the state map
    dill.dump(state_map,open(fileDir+"/resources/state.txt","w"),-1)

    # serialize the dma map
    dill.dump(dma_map,open(fileDir+"/resources/dma.txt","w"),-1)

    # Serialize the gender map
    dill.dump(gender_map,open(fileDir+"/resources/gender.txt","w"),-1)

    # Serialize the age map
    dill.dump(age_map,open(fileDir+"/resources/age.txt","w"),-1)









