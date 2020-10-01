import unittest
from source.AnimeIndexPage import _15_source
from common import web_utils, logging_utils, common_config

class Test_15(unittest.TestCase):
    def setUp(self):
        self.util = web_utils.Util()
        self.config = common_config.CommonConfig()
        self.log = logging_utils.LogTools()
        self.source = _15_source.Source_15()
        self.util.browser_start(self.config._15_url)

    def test_link_title(self):
        '''click the title link, contrast the new link and the expected link.
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

    def test_link_woyx_ts_1(self):
        '''
        click the wanouyouxi typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.woyx_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_woyx_detail(self):
        '''
        click the wanouyouxi detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.woyx_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.wanouyouxi_url)

    def test_link_shtx_ts_1(self):
        '''
        click the shouhutianxin typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.shtx_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_shtx_detail(self):
        '''
        click the shouhutianxin detail link, constrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.shtx_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shouhutianxin_url)

    def test_link_mksny_ts_1(self):
        '''
        click the mokashaonvying typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mksny_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_mksny_ts_2(self):
        '''
        click the mokashaonvying typestatistics GL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mksny_ts_GL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.GL_url)

    def test_link_mksny_ts_3(self):
        '''
        click the mokashaonvying typestatistics BL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mksny_ts_BL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BL_url)

    def test_link_mksny_ts_4(self):
        '''
        click the mokashaonvying typestatistics shoujiao link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mksny_ts_shoujiao_xpath)
        self.new_url = self.util.current_url

        self.assertEqual(self.new_url, self.config.shoujiao_url)

    def test_link_mksny_detail(self):
        '''
        click the mokashaonvying detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.mksny_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.mokashaonvying_url)

    def test_link_bsbndgs_ts_1(self):
        '''
        click the bishibinvdegushi typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.bsbndgs_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_bsbndgs_detail(self):
        '''
        click the bishibinvdegushi detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.bsbndgs_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.bishibinvdegushi_url)

    def test_link_gto_ts_1(self):
        '''
        click the gto typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.gto_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_gto_detail(self):
        '''
        click the gto detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.gto_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.GTO_url)

    def test_link_qccmd_ts_1(self):
        '''
        click the qingchuncaomeidan typestatistics weiGL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.qccmd_ts_weiGL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.weiGL_url)

    def test_link_qccmd_ts_2(self):
        '''
        click the qingchuncaomeidan typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.qccmd_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_qccmd_detail(self):
        '''
        click the qingchuncaomeidan detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.qccmd_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.qingchuncaomeidan_url)

    def test_link_flnh_ts_1(self):
        '''
        click the fanglangnanhai typestatistics BG link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.flnh_ts_BG_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BG_url)

    def test_link_flnh_ts_2(self):
        '''
        click the fanglangnanhai typestatistics qianzaiBL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.flnh_ts_qianzaiBL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.qianzaiBL_url)

    def test_link_flnh_detail(self):
        '''
        click the fanglangnanhai detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.flnh_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.fanglangnanhai_url)

    def test_link_fymzs_ts_1(self):
        '''
        click the fanglangnanhai typestatistics BL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.fymzs_ts_BL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.BL_url)

    def test_link_fymzs_detail(self):
        '''
        click the fengyumuzhishi detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.fymzs_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.fengyumuzhishi_url)

    def test_link_flcl_ts_1(self):
        '''
        click the FLCL typestatistics shuobuqingchu link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.flcl_ts_shuobuqingchu_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.shuobuqingchu_url)

    def test_link_flcl_detail(self):
        '''
        click the FLCL detail link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.flcl_detail_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.FLCL_url)

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
        click the typestatsitics GL link, contrast the new link and the expected link.
        '''
        self.util.click_xpath(self.source.ts_GL_xpath)
        self.new_url = self.util.current_url
        self.assertEqual(self.new_url, self.config.GL_url)

    def test_link_ts_qianzaiBL(self):
        '''
        click the typestatsitics qianzaiBL link, contrast the new link and the expected link.
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
        click the typestatistics shuobuqinchu link, contrast the new link and the expected link.
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


