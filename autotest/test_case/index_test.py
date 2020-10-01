import unittest
from source import index_source 
from common import web_utils, logging_utils, common_config

class Test_index(unittest.TestCase):
    def setUp(self):
        self.util = web_utils.Util()
        self.config = common_config.CommonConfig()
        self.log = logging_utils.LogTools()
        self.source = index_source.Source_index()
        self.util.browser_start(self.config.loveandlike_url)

    def tearDown(self):
        self.util.browser_quit()

    def test_link_title(self):
        '''
        click the title link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.title_AboutLoveAndLike_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.loveandlike_url) 
        
    def test_link_subtitle_1(self):
        '''
        click the subtitle 1 link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.subtitle_15_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config._15_url)

    def test_link_subtitle_2(self):
        '''
        click the subtitle 2 link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.subtitle_15to20_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config._15to20_url)

    def test_link_subtitle_3(self):
        '''
        click the subtitle 3 link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.subtitle_20to60_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config._20to60_url)

    def test_link_subtitle_4(self):
        '''
        click the subtitle 4 link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.subtitle_60_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config._60_url)

    def test_link_lyxxl_ts_1(self):
        '''click the langyuxiangxinliao typestatistics shenyuren link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.lyxxl_ts_shenyuren_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shenyuren_url)

    def test_link_lyxxl_ts_2(self):
        '''
        click the langyuxiangxinliao typestatistics shoujiao link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.lyxxl_ts_shoujiao_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shoujiao_url)

    def test_link_lyxxl_detail(self):
        '''
        click the langyuxiangxinliao'yuedugengduo button, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.lyxxl_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.langyuxiangxinliao_url)

    def test_link_yndj_ts_1(self):
        '''
        click the yiniandaiji typestatistics BG link,contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.yndj_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)
    
    def test_link_yndj_detail(self):
        '''
        click the yiniandaiji detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.yndj_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.yiniandaiji_url)

    def test_link_ts_BG(self):
        '''
        click the typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)
         
    def test_link_ts_BL(self):
        '''
        click the typestatistics BL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_BL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BL_url)

    def test_link_ts_GL(self):
        '''
        click the typestatistics GL link,contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_GL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.GL_url)

    def test_link_ts_qianzaiBL(self):
        '''
        click the typestatistics qianzaiBL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_qianzaiBL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.qianzaiBL_url)

    def test_link_ts_shoujiao(self):
        '''
        click the typestatistics shoujiao link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_shoujiao_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shoujiao_url)

    def test_link_ts_wangjixieleixingle(self):
        '''
        click the typestatistics wangjixieleixingle link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_wangjixieleixingle_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.wangjixieleixingle_url)

    def test_link_ts_shenyuren(self):
        '''
        click the typsstatistics shenyuren link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_shenyuren_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shenyuren_url)

    def test_link_ts_shuobuqingchu(self):
        '''
        click the typestatistics shuobuqingchu link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_shuobuqingchu_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shuobuqingchu_url)

    def test_link_ts_weiGL(self):
        '''
        click the typestatistics weiGL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_weiGL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.weiGL_url)

    def test_link_bdtb_article(self):
        '''
        clic the baidutieba article link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.baidutieba_article_link_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.baidutieba_article_url)


