
from pageobject.close_popoup_page import popups_page
from common.base_page import BasePage
import time
from common.read_config import read_data


class popups(popups_page):
    """
    :return get_path:网址路径
            get_url:拼接所有的地址+token+路径
            close:执行关闭弹窗方法
    """
    def get_path(self,path):
        self.path = path#获取每个页面路径
        return self.path

    def get_Url(self):
        data = read_data()
        self.url = data["stagingData"]["url"]
        self.token = data["stagingData"]["token"]
        self.fhd_url = BasePage.get_url(self, url=self.url, token=self.token)+self.path#拼接url
        return self.fhd_url

    def close(self):
        self.driver.delete_all_cookies()#清除浏览器cookies
        self.driver = BasePage.open(self,url=self.fhd_url)#打开URL
        time.sleep(3)
        popups_page.close_Popoup(self.driver)#执行关闭弹窗操作
        return self.driver


# class test_popoup:
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = WDriver.run_driver()
#
#         logger.info("启动浏览器成功")
#     def setUp(self):
#         self.open = popoup(self.driver)
#         self.open.open(url=rateManage_url+path)
#
#
#         logger.info("打开网页正常")
#         logger.info('************************starting run test cases************************')
#         return self.driver
#     #
#     # @classmethod
#     # def tearDowClass(cls):
#     #     popoup.open(cls.driver).quit()
#     #
#
#     def test_closse_popoup(self):
#        popoup(self.driver).close_Popoup()

#
if __name__ == '__main__':
    a = popups()
    a.close()

