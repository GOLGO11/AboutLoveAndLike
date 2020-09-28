import unittest
from BeautifulReport import BeautifulReport

from test_case.index_test import Test_index

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Test_index))
    result = BeautifulReport(suite)
    result.report(filename='test_report', description='index_page', log_path='./test_report/')
