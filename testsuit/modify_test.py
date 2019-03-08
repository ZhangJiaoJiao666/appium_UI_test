from pageobject.homepage import HomePage
from testsuit.basecase import BaseTestCase
from framework.logger import Logger
import unittest
import time

logger=Logger(logger="ModifyTest").getLog()
class ModifyTest(BaseTestCase):
    def test_modity(self):
        """修改功能"""
        h=HomePage(self.driver)
        modifyName='Lisa'
        h.modify(modifyName)
        # realName=h.alert_userName()
        # try:
        #     self.assertEqual(modifyName,realName,msg="")
        #     logger.info("修改成功！")
        # except Exception as e:
        #     logger.error("修改失败！")
        # time.sleep(6)
        h.logout()
if __name__=="__main__":
    unittest.main(verbosity=2)



