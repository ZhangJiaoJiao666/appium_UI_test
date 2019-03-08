from pageobject.homepage import HomePage
from testsuit.basecase import BaseTestCase
from framework.logger import Logger
import unittest

logger=Logger(logger="SearchTest").getLog()

class SerchTest(BaseTestCase):
    def test_search(self):
        '''搜索功能'''
        homePage=HomePage(self.driver)
        content="pppp"
        homePage.search(content)
        try:
            self.assertIn(content,self.driver.page_source,msg="")
            logger.info("搜索成功")
        except Exception as e:
            logger.error("未找到搜索内容",e)

if __name__=="__main__":
    unittest.main(verbosity=2)





