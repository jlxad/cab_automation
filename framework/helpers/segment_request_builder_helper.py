
# Brand, Category Pattern (id,minfreq,duration,timeofday,dayofweek)
def build_request_payload_for_segment_size_post(mtype,token_map):

    if mtype is None and len(token_map) is 1:
        for key in token_map:
            key1 = key
            value1 = token_map[key1]
            for key in value1:

                if key == "direct":

                    if key == "direct" and (key1 != "brand" or key1 != "category"):
                        main_type = key1
                        value_list = value1[key]
                        main_value = value_list[0]

                    if key == "direct" and (key1 == "brand" or key1 == "category"):
                        main_type = key1
                        val_list = value1[key][0].split("|")
                        main_value= {"id":val_list[0],"minfreq":val_list[1],
                                                  "duration": val_list[2],"timeofday":val_list[3],
                                                  "dayofweek":val_list[4]}
                else:
                    if key is not "brand" and key is not "category":
                            main_value_list = []
                            value_list = value1[key]
                            for ele in value_list:
                                dict1 = dict()
                                dict1['type'] = key
                                dict1['value'] = ele
                                main_value_list.append(dict1)
                            main_value = main_value_list
                            main_type = key1
                    else:
                       list1 = value1[key]
                       value_list = []

                       for i in list1:
                            i_list = i.split("|")
                            map = dict()
                            map['type'] = key
                            map['value'] = {"id":i_list[0],"minfreq":i_list[1],
                                      "duration": i_list[2],"timeofday":i_list[3],
                                      "dayofweek":i_list[4]}
                            value_list.append(map)

                       main_type = key1
                       main_value = value_list

    else:

        main_value = []
        for key in token_map:

                key1 = key
                value1 = token_map[key1]
                main_type = mtype

                for key in value1:

                    key2 = key

                    if key2 == "direct" and key1 != "brand" and key1 != "category":

                        value = value1[key2]
                        if len(value) is 1:
                            dict1 = dict()
                            dict1['type'] = key1
                            dict1['value'] = value[0]
                            main_value.append(dict1)

                    elif key2 == "direct" and key1 == "brand":

                        value = value1[key2]
                        val_list = value[0].split("|")
                        if len(value) is 1:
                            dict1 = dict()
                            dict1['type'] = key1
                            dict1['value'] = {"id": val_list[0], "minfreq": val_list[1],
                                              "duration": val_list[2],"timeofday": val_list[3],
                                              "dayofweek": val_list[4]}
                            main_value.append(dict1)

                    elif key2 == "direct" and key1 == "category":

                        value = value1[key2]
                        val_list = value[0].split("|")
                        if len(value) is 1:
                            dict1 = dict()
                            dict1['type'] = key1
                            dict1['value'] = {"id": val_list[0], "minfreq": val_list[1],
                                              "duration": val_list[2], "timeofday": val_list[3],
                                              "dayofweek": val_list[4]}
                            main_value.append(dict1)

                    elif key2 == "nested" and key1 != "NOT":
                        value=value1[key2]
                        main_dict = build_request_payload_for_segment_size_post(key1,value)
                        main_value.append(main_dict)

                    elif key2 == "nested" and key1 == "NOT":
                        value=value1[key2]
                        main_dict = build_request_payload_for_segment_size_post(key1,value)
                        main_dict['value'] = main_dict['value'][0]
                        main_value.append(main_dict)

                    else:

                        if key2 != "brand" and key2 != "category":

                            value = value1[key2]

                            if len(value) is 1:
                                list = value1[key]
                                dict1 = dict()
                                dict1['type'] = key1
                                map = dict()
                                map['type'] = key
                                map['value'] = list[0]
                                dict1['value'] = map
                                main_value.append(dict1)
                            else:

                                list1 = value1[key]
                                value_list = []
                                dict1 = dict()
                                dict1['type'] = key1

                                for i in list1:
                                    map = dict()
                                    map['type'] = key
                                    map['value'] = i
                                    value_list.append(map)
                                dict1['value'] = value_list
                                main_value.append(dict1)
                        else:

                            value = value1[key2]

                            if len(value) is 1:
                                list = value1[key]
                                val_list = list[0].split("|")
                                dict1 = dict()
                                dict1['type'] = key1
                                map = dict()
                                map['type'] = key
                                map['value'] = {"id":val_list[0],"minfreq":val_list[1],
                                              "duration": val_list[2],"timeofday":val_list[3],
                                              "dayofweek":val_list[4]}
                                dict1['value'] = map
                                main_value.append(dict1)
                            else:

                                list1 = value1[key]
                                value_list = []
                                dict1 = dict()
                                dict1['type'] = key1

                                for i in list1:
                                    i_list = i.split("|")
                                    map = dict()
                                    map['type'] = key
                                    map['value'] = {"id":i_list[0],"minfreq":i_list[1],
                                              "duration": i_list[2],"timeofday":i_list[3],
                                              "dayofweek":i_list[4]}
                                    value_list.append(map)
                                dict1['value'] = value_list
                                main_value.append(dict1)

    request = {
                    "type": main_type,
                    "value": main_value
              }
    return request









