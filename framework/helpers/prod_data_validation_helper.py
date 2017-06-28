from framework.helpers.mysql_helper import *
from texttable import Texttable
from dictionary_query_builder import *

t = Texttable()
t.add_row(['Query', 'Previous_build_count', 'New_build_count', 'Difference_in_Count'])


def compare_current_and_previous_run_results_in_prod(count, query_number, desc_query):
    # Get the count recorded from the previous run and verify it with the new count from the current run.
    cnx = mysql_connect("test_cab", "qa")
    query = "select * from prod_data where query_id='" + query_number + "' ORDER BY id DESC LIMIT 1"
    data = get_row_from_results(cnx, query)
    previous_day_count = data['user_count']
    today_count = count
    diff = int(today_count) - int(previous_day_count)

    # Insert the records into the text table
    t.add_row([desc_query, previous_day_count, today_count, diff])

    # Insert the record into the db
    now = datetime.datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M")
    cur = cnx.cursor(dictionary=True)
    cur.execute("INSERT INTO prod_data (query_id, query, generated_date, user_count) VALUES (%s,%s,%s,%s) ",
                (query_number, desc_query, current_date_time, count))
    cnx.commit()
    cnx.close()

    if today_count != previous_day_count:

        # Get the threshold value
        data = read_data_from_config_json("config.json")
        # If the difference is more than 20% raise an exception
        if diff > (data['percentage_threshold_production'] / 100) * int(previous_day_count):
            raise Exception(" There is something going wrong with the data;User count from previous day =" + str(
                previous_day_count) + ":: User count from today = " + str(today_count))
