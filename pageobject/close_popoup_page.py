from common.base_page import BasePage
from common.Logger import logger
from data.popups_data import PopupswindowsPageData
class popups_page(BasePage):

    """获取弹窗然后点击关闭按钮"""

    def close_xbtn(self):
       BasePage.click(self,PopupswindowsPageData.close_btn_selectors)

    def close_abtn(self):
        BasePage.click(self,PopupswindowsPageData.close_Abtn_selectors)

    def announcement_popup(self):
        try:
            if BasePage.find_element(self,PopupswindowsPageData.announcement_selectors):
                self.close_abtn()
        except:
            logger.info("找不到公告弹窗")

    def Pay_popup(self):
        try:
            if BasePage.find_element(self,PopupswindowsPageData.Pay_popup_selectors):
                self.close_xbtn()
        except:
            logger.info("找不到广告弹窗")

    def close_Popoup(self):
          while True:
              try:
                  if self.announcement_popup():
                      continue
                  elif self.Pay_popup():
                        continue

              except:

                  logger.info("没有找到弹窗进行后续操作")
                  break