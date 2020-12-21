import unittest
from source.AnimeIndexPage import _15to20_source
from common import web_utils, logging_utils, common_config

class Test_15to20(unittest.TestCase):
    def setUp(self):
        self.util = web_utils.Util()
        self.config = common_config.CommonConfig()
        self.log = logging_utils.LogTools()
        self.source = _15to20_source.Source_15to20()
        self.util.browser_start(self.config._15to20_url)

    def test_link_title(self):
        '''
        click the title link, contrast the new link and expected link.
        '''
        self.util.click_xpath(self.source.title_AboutLoveAndLike_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.loveandlike_url)

    def test_link_subtitle_1(self):
        '''
        click the subtitle 1 link. contrast the new link and the expected link.
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

    def test_link_jbcm_ts_1(self):
        '''
        click the jingbaocaomei GL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.jbcm_ts_GL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.GL_url)

    def test_link_jbcm_detail(self):
        '''
        click the jingbaocaomei detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.jbcm_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.jingbaocaomei_url)

    def test_link_fyqj_ts_1(self):
        '''
        click the fengyaquanji BG link, contrast the new link and the expected  link.
        '''
        self.util.click_xpath(self.source.fyqj_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_fyqj_detail(self):
        '''
        click the fengyaquanji detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.fyqj_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.fengyaquanji_url)

    def test_link_mzbnx_ts_1(self):
        '''
        click the mizhibinvx typetsatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mzbnx_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_mzbnx_detail(self):
        '''
        click the mizhibinvx detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mzbnx_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.mizhibinvx_url)

    def test_link_wxsn_ts_1(self):
        '''
        click the wenxueshaonv typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.wxsn_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_wxsn_detail(self):
        '''
        click the wenxueshaonv detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.wxsn_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.wenxueshaonv_url)

    def test_link_ispure_ts_1(self):
        '''
        click the I's pure typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ispure_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_ispure_detail(self):
        '''
        click, the I's pure detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ispure_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.Is_pure_url)

    def test_link_xymhdw_ts_1(self):
        '''
        click the xiaoyuanmihudawang typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.xymhdw_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_xymhdw_detail(self):
        '''
        click the xiaoyuanmihudawang detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.xymhdw_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.xiaoyuanmihudawang_url)

    def test_link_laqj_ts_1(self):
        '''
        click the lianaiqingjie typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.laqj_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_laqj_detail(self):
        '''
        click the lianaiqingjie detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.laqj_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.lianaiqingjie_url)

    def test_link_tgsn_ts_1(self):
        '''
        click the tianguoshaonv typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.tgsn_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_tgsn_detail(self):
        '''
        click the tianguoshaonv detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.tgsn_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.tianguoshaonv_url)

    def test_link_hldtz_ts_1(self):
        '''
        click the hualidetiaozhan typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.hldtz_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_hldtz_detail(self):
        '''
        click the hualidetiaozhan detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.hldtz_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.hualidetiaozhan_url)

    def test_link_beck_ts_1(self):
        '''
        click the beck typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.beck_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_beck_detail(self):
        '''
        click the beck detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.beck_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.beck_url)

    def test_link_ywbydyk_ts_1(self):
        '''
        click the yangwangbanyuedeyekong typestatistics BG link, contrast the new link and the expected lnk.
        '''
        self.util.click_xpath(self.source.ywbydyk_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_ywbydyk_detail(self):
        '''
        click the yangwangbanyuedeyekong detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ywbydyk_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.yangwangbanyuedeyekong_url)

    def test_link_h2o_ts_1(self):
        '''
        click the h2o chishayinji typestatistics wangjixieleixingle link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.H2O_ts_wjxlxl_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.wangjixieleixingle_url)

    def test_link_h2o_detail(self):
        '''
        click the h2o chishayinji detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.H2O_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.H2Ochishayinji_url)

    def test_link_sglz_ts_1(self):
        '''
        click the shuiguolanzi typestatistics shoujiao link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.sglz_ts_shoujiao_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shoujiao_url)

    def test_link_sglz_detail(self):
        '''
        click the shuiguolanzi detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.sglz_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shuiguolanzi_url)

    def test_link_ys_ts_1(self):
        '''
        click the yingshou typestatistics BL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ys_ts_BL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BL_url)

    def test_link_ys_detail(self):
        '''
        click the yingshou detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ys_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.yingshou_url)

    def test_link_qjskc_ts_1(self):
        '''
        click the quanjinshukuangchao typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.qjskc_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_qjskc_detail(self):
        '''
        click the quanjinshukuangchao detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.qjskc_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.quanjinshukuangchao_url)

    def test_link_thyd_ts_1(self):
        '''
        click the taohuayuedan typestatistics shuobuqingchu link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.thyd_ts_sbqc_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shuobuqingchu_url)

    def test_link_thyd_detail(self):
        '''
        click the taohuayuedan detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.thyd_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.taohuayuedan_url)

    def test_link_munto_ts_1(self):
        '''
        click the munto typestatistics shenyuren link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.munto_ts_shenyuren_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shenyuren_url)

    def test_link_munto_detail(self):
        '''
        click the munto detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.munto_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.munto_url)

    def test_link_yndj_ts_1(self):
        '''
        click the yiniandaiji typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.yndj_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_yndj_detail(self):
        '''
        click the yiniandaiji detail link, contrast the new link and the expected link,
        '''
        self.util.click_xpath(self.source.yndj_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.yiniandaiji_url)

    def test_link_cygwy_ts_1(self):
        '''
        click the caiyunguowuyu typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.cygwy_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_cygwy_detail(self):
        '''
        click the caiyunguowuyu detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.cygwy_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.caiyunguowuyu_url)

    def test_link_wldsn6_ts_1(self):
        '''
        click the weilaidushiNO.6 typestatistics BL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.wldsn6_ts_BL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BL_url)

    def test_link_wldsn6_detail(self):
        '''
        click the weilaidushiNO.6 detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.wldsn6_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.weilaidushiNO6_url)

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
        click the typestatistics shoujiao link, contrast the new link and the expected  link.
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

    def tearDown(self):
        self.util.browser_quit()
