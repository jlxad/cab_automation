from framework.helpers.segment_request_builder_helper import *
from framework.helpers.dictionary_query_builder import *
import requests
import logging
import json

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger = logging.getLogger("cab.helpers.segmentsizehelper")

def segment_size_post(main_type,generic_input_dict,db_validation):

    request = build_request_payload_for_segment_size_post(main_type,generic_input_dict)
    request_obj = json.dumps(request).replace("l:","")
    path = API_URL + "/segment_size?query="+str(request_obj)

    logger.debug("Request Path: "+path)

    if request_obj is not None:
        logger.debug("Request Body: " +request_obj)

        response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))

    if response.status_code is 200 and if "num_audience" in response.json():

       response_result = response.json()['num_audience']
       logger.info("Audience count from the response- "+str(response_result))
       response_time = response.json()['response_time']

       # # Make sure that the response time is less than 500 ms
       # response_time_final = response_time.replace("us","")
       # if int(response_time_final) > 500000:
       #   raise Exception(" The response time cannot be more than 500 milliseconds")

       if db_validation is True:

           # if main_type is None and len(generic_input_dict) is 1:
               for key in generic_input_dict:
                   val = generic_input_dict[key]
                   for key1 in val:
                       val_list = val[key1]
                       if key1 == "direct" and len(val_list) is 1:
                           num_from_dict = get_result_from_dictionary_single_row(main_type,generic_input_dict)
                       if key1 != "direct" and len(val_list) > 1:
                            num_from_dict = get_result_from_dictionary_single_row_logical_operations(main_type,generic_input_dict)

               logger.info("Audience count from dictionary- "+str(num_from_dict))
               if int(response_result) != int(num_from_dict):
                   raise Exception("The number of the audience from the endpoint does not match "
                                   "with the result from the dictionary")
       return response_result

    else:
       logger.info("num Audience is not found due to errorcode " + str(response.json()["ecode"]) + ": " + str(response.json()["edesc"]))
       raise Exception("Response contains errors")

def data_provider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test"""
    def test_decorator(fn):
        def repl(self, *args, **kwargs):
            vals = fn_data_provider()
            for i in range(0, len(vals)):
                if i != 0:
                    self.setUp()
                try:
                    fn(self, *vals[i], **kwargs)
                except AssertionError:
                    print("Assertion error caught with data set ", i)
                    raise
                finally:
                    if i != len(vals)-1:
                        self.tearDown()
        return repl
    return test_decorator




