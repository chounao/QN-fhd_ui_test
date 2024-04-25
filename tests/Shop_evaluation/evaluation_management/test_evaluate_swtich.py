import pytest
import time
from pageobject.shop_evaluation_page.evalution_management_page.rateManage_Top_page import touch_switch
from tests.Shop_evaluation.conftest import Test_popups

class Test_automatic_evaluation(touch_switch):

    def test_touch_evaluSwtich(self):
        self.driver = Test_popups.test_closepopus(self)
        before_status = touch_switch.get_evalu_switch(self).text
        touch_switch.touch_eavaluation_swicth(self)
        later_status = touch_switch.get_evalu_switch(self).text
        assert later_status != before_status


