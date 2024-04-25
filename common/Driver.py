"""
打开网页

"""
import os
from selenium import webdriver
from common.Logger import logger


import platform
class WDriver:


    def run_driver(self):

        """

        :return: platform.system() 当前系统Windows系统下运行返回 'Windows'，Linux返回'Linux'，MacOS返回'Darwin'
        """

        self.platform = platform.system()
        logger.info("获取到当前操作系统为%s" % self.platform)
        try:
            if self.platform == "Windows":

                self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

            elif self.platform == "Darwin":
                self.driver = webdriver.Chrome()
        except Exception as e:
            logger.exception('ChromeDriverServer.exe executable needs to be in PATH. Please download!',
                             exc_info=True)
            raise e
        else:
            logger.info('found the chrome driver [%s] successed !' % self.driver)
            return self.driver


if __name__ == '__main__':
    WDrive=WDriver()
    WDrive.run_driver()