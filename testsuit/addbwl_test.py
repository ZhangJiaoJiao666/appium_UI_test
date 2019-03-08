from testsuit.basecase import BaseTestCase
from pageobject.homepage import HomePage
from framework.logger import Logger
import unittest

logger=Logger(logger="AddbmlTest").getLog()
class AddbwlTest(BaseTestCase):
    def test_bwl(self):
        """添加备忘录"""
        homePage=HomePage(self.driver)
        content="2019.03.07,18:38"
        secondContent="this is the second bwl"
        homePage.bwl(content)
        try:
            self.assertIn(content,self.driver.page_source,msg="")
            logger.info("添加备忘录成功")
        except Exception as e:
            logger.error("添加备忘录失败！")

        homePage.bwltwo(secondContent)
        try:
            self.assertIn(secondContent,self.driver.page_source,msg="")
            logger.info("第二种添加备忘录成功")
        except Exception as e:
            logger.error("添加备忘录失败！")

if __name__=="__main__":
    unittest.main(verbosity=2)


