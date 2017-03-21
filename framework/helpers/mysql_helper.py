from mysql.connector import (connection)

def mysql_connect(db_name):

    cnx = connection.MySQLConnection(user='root',
                                         password='venableroot',
                                         host='ec2-52-39-137-40.us-west-2.compute.amazonaws.com',
                                         port=3336,
                                         database=db_name)
    return cnx

def mysql_connect_prod(db_name):

    cnx = connection.MySQLConnection(user='apps',
                                         password='appsxaddb',
                                         host='app-int.db.xad.com',
                                         port=3336,
                                         database=db_name)
    return cnx



def mysql_close_connection(cnx):
    cnx.close()


def get_result(cnx,query):

    sql = query
    cur = cnx.cursor(dictionary=True)
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        return row

def get_all_result(cnx,query):

    sql = query
    cur = cnx.cursor(dictionary=True)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def get_result_set_list(cnx,query, col_name):

    list = []
    sql = query
    cur = cnx.cursor(dictionary=True)
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        list.append(row[col_name])
    list.sort()
    return list