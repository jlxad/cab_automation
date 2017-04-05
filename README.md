------------------------------------------------------
         Steps to run the automated test cases
------------------------------------------------------

Tests Location : The test cases are under the directory of cab_automation starting with the name "test_"

The automated test cases can be run against various environments like qe, dev and prod. Before running the test cases, make sure to modify the API_URL variable in config.py.

Important: For the tests to run, the test data has to be loaded under resources folder with the name "dump.txt". This data partition is from s3.

----------------------------------------------------------
How to run the tests via Pycharm in various environments?
----------------------------------------------------------

How to run the tests in a particular test class in the IDE?

  - Right click a particular test class and Click Run to run all the test cases in a particular test class.

----------------------------------
How to run the tests via Terminal?
----------------------------------

How to run one particular test inside a test class?

    - Step 1: cd cab_automation
    - Step 2: Run the command : python testfilename testclassname.testcasename
              e.g python test_segment_size_post.py SegmentSizePostTests.test_users_in_country_us

How to run all the tests in a particular test class?

     - Step 1: cd cab_automation
     - Step 2: Run the command : python testfilename testclassname
               e.g python test_segment_size_post.py SegmentSizePostTests





