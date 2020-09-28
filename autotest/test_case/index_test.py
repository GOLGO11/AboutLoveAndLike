import unittest
from source import index_source 
from common import web_utils, logging_utils, common_config

class Test_index(unittest.TestCase):
    def setUp(self):
        self.util = web_utils.Util()
        self.config = common_config.CommonConfig()
        self.log = logging_utils.LogTools()
        self.source = index_source.Source_index()
        self.util.browser_start(self.config.index_url)

    def tearDown(self):
        self.util.browser_quit()

    def test_link_title(self):
        '''click the title link, contrast the new link and the expected link'''

        self.util.click_xpath(self.source.title_AboutLikeAndLove_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.index_url)
        self.log.info('new_url   ' + self.new_url)

    def test_link_subtitle_1(self):
        '''click the subtitle link,contrast the new link and the expected link'''
        pass
