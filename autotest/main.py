import unittest
from BeautifulReport import BeautifulReport

from test_case.index_test import Test_index
from test_case.AnimeIndexPage._15_test import Test_15

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTests(unittest.makeSuite(Test_index))
    suite.addTests(unittest.makeSuite(Test_15))
    #suite.addTest(Test_15("test_link_subtitle_2"))
    result = BeautifulReport(suite)
    result.report(filename='test_report', description='index_page_test', log_path='./test_report/')
