from tests.conftest import popups
class Test_popups(popups):

   def test_closepopus(self):
      path = "#/v5/rateManage"
      self.path = popups.get_path(self,path=path)
      self.url = popups.get_Url(self)
      self.driver = popups.close(self)
      return self.driver


class Test_UI(popups):
   @classmethod
   def setUpClass(cls):
      Test_popups.test_closepopus()

   @classmethod
   def tearDownClass(cls):
      
      popups.quit()

if __name__ == '__main__':
    a = Test_popups()
    a.test_closepopus()