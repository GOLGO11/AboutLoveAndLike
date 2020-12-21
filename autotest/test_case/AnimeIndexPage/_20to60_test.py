import unittest
from source.AnimeIndexPage import _20to60_source
from common import web_utils, logging_utils, common_config

class Test_20to60(unittest.TestCase):
    def setUp(self):
        self.util = web_utils.Util()
        self.config = common_config.CommonConfig()
        self.log = logging_utils.LogTools()
        self.source = _20to60_source.Source_20to60()
        self.util.browser_start(self.config._20to60_url)

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

    def test_link_fmysyc_ts_1(self):
        '''
        click the fengmiyusiyecao typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.fmysyc_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_fmysyc_detail(self):
        '''
        click the fengmiyusiyecao detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.fmysyc_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.fengmiyusiyecao_url)

    def test_link_lf_ts_1(self):
        '''
        click the lianfeng typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.lf_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_lf_detail(self):
        '''
        click the lianfeng detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.lf_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.lianfeng_url)

    def test_link_jxqrm_ts_1(self):
        '''
        click the jiaoxiangqingrenmeng typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.jxqrm_ts_BG_xpath)
        self.new_url = self.util.current_url 
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_jxqrm_detail(self):
        '''
        click the jiaoxiangqingrenmeng detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.jxqrm_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.jiaoxiangqingrenmeng_url)

    def test_link_nana_ts_1(self):
        '''
        click the nana typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.nana_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_nana_detail(self):
        '''
        click the nana detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.nana_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.nana_url)

    def test_link_ttzw_ts_1(self):
        '''
        click the tiantangzhiwen typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ttzw_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_ttzw_detail(self):
        '''
        click the tiantangzhiwen detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ttzw_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.tiantangzhiwen_url)

    def test_link_ezjzw_ts_1(self):
        '''
        click the ezuojuzhiwen typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ezjzw_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_ezjzw_detail(self):
        '''
        click the ezuojuzhiwen detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ezjzw_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.ezuojuzhiwen_url)

    def test_link_xxmh_ts_1(self):
        '''
        click the xiaxuemihui typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.xxmh_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_xxmh_detail(self):
        '''
        click the xiaxuemihui detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.xxmh_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.xiaxuemihui_url)

    def test_link_tsgzz_ts_1(self):
        '''
        click the tushuguanzhanzheng typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.tsgzz_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_tsgzz_detail(self):
        '''
        click the tushuguanzhanzheng detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.tsgzz_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.tushuguanzhanzheng_url)

    def test_link_ykw_ts_1(self):
        '''
        click the yankuwang typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ykw_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_ykw_ts_2(self):
        '''
        click the yankuwang typestatistics BL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ykw_ts_BL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BL_url)

    def test_link_ykw_detail(self):
        '''
        click teh yankuwang detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ykw_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.yankuwang_url)

    def test_link_lkjxzyp_ts_1(self):
        '''
        click the langkejianxinzhuiyipian typestatistics BG link, contrast the new link and the expected link
        '''
        self.util.click_xpath(self.source.lkjxzyp_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_lkjxzyp_detail(self):
        '''
        click the langkejianxinzhuiyipian detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.lkjxzyp_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.langkejianxinzyp_url)

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
        click the typestatistics GL link, contrast the new link and the expected link.
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
        click the typestatistics shenyuren link, contrast the new link and the expected link.
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
        click the baidutieba article link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.baidutieba_article_link_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.baidutieba_article_url)

    def teatDown(self):
        self.util.browser_quit()
