from common.base_page import BasePage
from common.Logger import logger
from data.shop_evaluation_data.evalution_mangment_data.rateManage_data import Switch_btn
from selenium.webdriver.common.by import By
from tests.Shop_evaluation.conftest import Test_popups
import time
class touch_switch(BasePage):

    def get_evalution(self):
        #获取模块
        self.evaluation = BasePage.find_element(self,Switch_btn.evaluation_data_selects)
        return self.evaluation

    def get_evalupage_text(self):
        # 获取模块字段
        self.evalu_text=self.get_evalution().find_element(By.CLASS_NAME,"text").text
        logger.info(self.evalu_text)
        return self.evalu_text

    def get_evalu_switch(self):
        #获取按钮
        self.evalu_switch = self.get_evalution().find_element(By.CLASS_NAME,"ant-switch-inner")
        return  self.evalu_switch

    def get_popup_winds(self):
        #弹窗
        self.popuo_winds=BasePage.find_element(self,Switch_btn.popup_winds_selects)
        logger.info("获取到弹窗")
        return self.popuo_winds
    def click_determine_btn(self):
        #确定按钮
        BasePage.click(self,Switch_btn.determine_btn_selects)
        logger.info("点击确定按钮")

    def get_remind(self):
        #获取中差评模块
        self.remind=BasePage.find_element(self,Switch_btn.remind_data_selects)
        return self.remind

    def get_remind_text(self):
        #获取中差评text
        self.remind_text = self.get_remind().find_element(By.CLASS_NAME, "text").text
        logger.info(self.remind_text)
        return self.remind_text

    def get_remind_switch(self):
        #获取中差评按钮
        self.remind_switch = self.get_remind().find_element(By.CLASS_NAME, "ant-switch-inner")
        return self.remind_switch

    def click_all_open(self):
        #一键开启

        self.all_open = self.get_popup_winds().find_element(By.CLASS_NAME, "allOpen")

        logger.info("点击一键开启按钮")
        return self.all_open







    def touch_eavaluation_swicth(self):

        self.get_evalupage_text()
        try:
            if self.get_evalu_switch().text == "已关闭":
                """开启操作"""
                try:
                    self.evalu_switch.click()
                    logger.info("自动评价成功开启")
                except:
                    logger.info("自动评价无法点击开启按钮")
            elif self.evalu_switch.text == "已开启":
                """关闭操作"""
                try:
                    self.evalu_switch.click()

                    time.sleep(0.5)
                    self.click_determine_btn()
                    logger.info("自动评价已经关闭")
                except:
                    logger.info("自动评价无法点击关闭按钮")
        except:
            logger.info("自动评价无法获取到自动评价按钮状态")

    def touch_remind_switch(self):
        self.driver = Test_popups.test_closepopus(self)
        self.get_remind_text()
        try:
            if self.get_remind_switch().text =="已开启":
                """关闭操作"""
                try:
                    self.remind_switch.click()
                    time.sleep(0.5)
                    self.click_determine_btn()
                    logger.info("中差评提醒成功关闭")
                except:
                    logger.info("中差评提醒关闭操作失败")
            if self.get_remind_switch().text== "已关闭" and self.get_evalu_switch().text == "已开启":
                """开启操作"""
                try:
                    self.remind_switch.click()
                    logger.info("中差评提醒成功开启")
                except:
                    logger.info("中差评提醒开启操作失败")
            if self.get_remind_switch().text== "已关闭" and self.get_evalu_switch().text =="已关闭":
                """一键开启"""
                try:
                    self.remind_switch.click()
                    time.sleep(1)
                    self.click_all_open()
                    logger.info("中差评提醒和自动评价成功开启")
                except:
                    logger.info("一键开启操作失败")
        except:
            logger.info("中差评提醒操作失败")






if __name__ == '__main__':
    # a = te_1()
    # a.get_a()

    a = touch_switch()
    a.touch_remind_switch()







