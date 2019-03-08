from testsuit.basecase import BaseTestCase
from pageobject.homepage import HomePage
from ddt import ddt,unpack,data
from framework.logger import Logger
from framework.utils import Utils
import unittest
import time

datatest=Utils.read_excel("E:/appium_UI_test_memo/data/data.xlsx", "Sheet1")
logger=Logger(logger="LoginTest").getLog()
@ddt
class LoginTest(BaseTestCase):
    @data(*datatest)
    def test_login(self,data):
        '''登录功能'''
        home=HomePage(self.driver)
        userName = data['email']
        pwd = int(data['password'])
        home.login(userName,pwd)
        realName=home.alert_userName()
        try:
            self.assertEqual(realName,"Lisa",msg="成功")
            logger.info("登录成功")
        except Exception as e:
            logger.error("登录失败！",e)
        time.sleep(4)
        home.logout()

if __name__=="__main__":
    unittest.main(verbosity=2)








