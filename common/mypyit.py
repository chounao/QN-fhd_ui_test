import Driver
import pytest
from common.Logger import logger
import base_page


class MypyTest():

    @classmethod
    def setUpClass(cls):# 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间
        cls.driver = Driver.WDriver.run_driver()
        cls.driver.maximize_window()
        logger.info("opened the browser successed")


    def setUp(self):
        """

        :return:
        """

        logger.info('************************starting run test cases************************')


    def tearDonw(self):
        """

        :return:
        """
        self.driver.refresh()
        logger.info('************************test case run completed************************')


    @classmethod
    def tearDonwClass(cls):
        cls.driver.quit()
        logger.info('quit the browser success!')
