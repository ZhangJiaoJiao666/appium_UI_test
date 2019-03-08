from pageobject.homepage import HomePage
from testsuit.basecase import BaseTestCase
import unittest
import time
from framework.logger import Logger
logger=Logger(logger="RegistTest").getLog()
class RegistTest(BaseTestCase):
    def test_all(self):
        '''注册功能'''
        homePage=HomePage(self.driver)
        r_nickName="zhang"
        r_email="100434543@163.com"
        r_pwd="12346789"
        homePage.registSuccess(r_nickName,r_email,r_pwd)
        try:
            realName=homePage.alert_userName()
            self.assertEqual(r_nickName,realName,msg="")
            logger.info("注册成功!")
        except Exception as e:
            logger.error("注册失败！")







if __name__=="__main__":
    unittest.main(verbosity=2)
