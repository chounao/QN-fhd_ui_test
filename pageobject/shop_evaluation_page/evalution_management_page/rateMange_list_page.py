from common.base_page import BasePage
from common.Logger import logger
from data.shop_evaluation_data.evalution_mangment_data.rateManage_data import list
from selenium.webdriver.common.by import By
from tests.Shop_evaluation.conftest import Test_popups
import time

class list_touch(BasePage):
    def click_send_megs_btn(self):
        #批量发送短信按钮
        BasePage.click(self,list.send_megs_select)
    def click_synchro_btn(self):
        #手动同步
        BasePage.click(self,list.synchronization_btn_select)

    def send_megs(self):
        self.click_send_megs_btn()

    def synchro(self):
        Test_popups.test_closepopus(self)
        self.click_synchro_btn()
        time.sleep(9)
        self.click_synchro_btn()









if __name__ == '__main__':
    a= list_touch()
    a.synchro()