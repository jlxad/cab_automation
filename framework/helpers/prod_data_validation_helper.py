import datetime
from framework.helpers.mysql_helper import *
from prettytable import PrettyTable
from texttable import Texttable

t= Texttable()
t.add_row(['Query', 'Previous_build_count', 'New_build_count', 'Difference_in_Count'])


def verify_data_in_db_helper(count, query_number, desc_query):

    # Get the count recorded the previous run and verify it with the new count. If the difference is more than 10% raise an exception
    cnx = mysql_connect("test_cab")
    query = "select * from prod_data where query_id='"+query_number+"' ORDER BY id DESC LIMIT 1"
    data = get_result(cnx,query)
    previous_day_count = data['user_count']
    today_count = count
    diff = int(today_count)-int(previous_day_count)
    cnx.close()
    t.add_row([desc_query,previous_day_count,today_count,diff])

    # Insert the record into the db
    cnx = mysql_connect("test_cab")
    now = datetime.datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M")
    cur = cnx.cursor(dictionary=True)
    cur.execute("INSERT INTO prod_data (query_id, query, generated_date, user_count) VALUES (%s,%s,%s,%s) ", (query_number, desc_query, current_date_time, count))
    cnx.commit()
    cnx.close()

    if today_count != previous_day_count:
        if diff > (10/100)*int(previous_day_count):
            raise Exception(" There is something going wrong with the data;User count from previous day ="+str(previous_day_count)+":: User count from today = "+str(today_count))






