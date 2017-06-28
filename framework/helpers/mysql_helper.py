from mysql.connector import (connection)
import json


# Reading the config data from the config json file
def read_data_from_config_json(file_name):
    with open(file_name) as json_data_file:
        data = json.load(json_data_file)
    return data


# Establishing mysql connection
def mysql_connect(db_name, env):
    mysql_config_data = read_data_from_config_json('config.json')
    cnx = connection.MySQLConnection(user=mysql_config_data['mysql'][env]['user'],
                                     password=mysql_config_data['mysql'][env]['password'],
                                     host=mysql_config_data['mysql'][env]['host'],
                                     port=mysql_config_data['mysql'][env]['port'],
                                     database=db_name)
    return cnx


# Close mysql connection
def mysql_close_connection(cnx):
    cnx.close()


# Get a single row from the result set
def get_row_from_results(cnx, query):
    result = get_results_sql_query(cnx, query)
    for row in result:
        return row


# Get all the results from the result set
def get_results_sql_query(cnx, query):
    sql = query
    cur = cnx.cursor(dictionary=True)
    cur.execute(sql)
    result = cur.fetchall()
    return result


# Get all the values of a particular column sorted from the result set and stored in a list
def get_sorted_column_values_in_list(cnx, query, col_name):
    result = get_results_sql_query(cnx, query)
    for row in result:
        list.append(row[col_name])
    list.sort()
    return list
