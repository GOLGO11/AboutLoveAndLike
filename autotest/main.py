import unittest
from BeautifulReport import BeautifulReport

from test_case.index_test import Test_index
from test_case.AnimeIndexPage._15_test import Test_15
from test_case.AnimeIndexPage._15to20_test import Test_15to20
from test_case.AnimeIndexPage._20to60_test import Test_20to60
from test_case.AnimeIndexPage._60_test import Test_60

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTests(unittest.makeSuite(Test_index))
    #suite.addTests(unittest.makeSuite(Test_15))
    #suite.addTest(Test_15("test_link_subtitle_2"))
    #suite.addTests(unittest.makeSuite(Test_15to20))
    #suite.addTests(unittest.makeSuite(Test_20to60))
    suite.addTests(unittest.makeSuite(Test_60))
    result = BeautifulReport(suite)
    result.report(filename='test_report', description='index_page_test', log_path='./test_report/')
