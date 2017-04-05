import unittest
import xmlrunner
from test_segment_size_post import SegmentSizePostTests
from test_segment_size_post_brands_saturdays import SegmentSizePostBrandsSaturdayTests
from test_segment_size_post_brands_sundays import SegmentSizePostBrandsSundayTests
from test_segment_size_post_brands_weekdays import SegmentSizePostBrandsWeekdayTests
from test_segment_size_post_brands_weekends import SegmentSizePostBrandsWeekendTests
from test_segment_size_post_categories_saturdays import SegmentSizePostCategorySaturdayTests
from test_segment_size_post_categories_sundays import SegmentSizePostCategorySundayTests
from test_segment_size_post_categories_weekdays import SegmentSizePostCategoryWeekdayTests
from test_segment_size_post_categories_weekends import SegmentSizePostCategorysWeekendTests


if __name__ == "__main__":

    test_classes_to_run = [SegmentSizePostTests,SegmentSizePostBrandsSaturdayTests,SegmentSizePostBrandsSundayTests,
                           SegmentSizePostBrandsWeekendTests,SegmentSizePostBrandsWeekdayTests,
                           SegmentSizePostCategorySaturdayTests,SegmentSizePostCategorySundayTests,
                           SegmentSizePostCategoryWeekdayTests,SegmentSizePostCategorysWeekendTests
                           ]

    loader = unittest.TestLoader()

    suite_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suite_list.append(suite)

    big_suite = unittest.TestSuite(suite_list)
    runner=xmlrunner.XMLTestRunner(output='test-reports')
    runner.run(big_suite)

# import unittest
# import xmlrunner
# from test_segment_size_post import SegmentSizePostTests
#
# def suite():
#
#     suite = unittest.TestSuite()
#
#     # Login
#     suite.addTest(SegmentSizePostTests('test_users_in_country_us'))
#     return suite
#
#
#
# if __name__ == "__main__":
#     runner=xmlrunner.XMLTestRunner(output='test-reports')
#     test_suite = suite()
#     runner.run(test_suite)


