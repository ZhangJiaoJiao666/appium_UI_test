from pageobject.homepage import HomePage
from testsuit.basecase import BaseTestCase
from framework.logger import Logger
import unittest

logger=Logger(logger="DeleteTest").getLog()
class DeleteTest(BaseTestCase):
    def test_delete(self):
        """删除和清空功能"""
        h=HomePage(self.driver)
        length = h.alert_delete() #删除前备忘录的总长度
        h.deletei()
        finLength=h.alert_delete() #删除后的长度
        try:
            self.assertGreater(length,finLength)
            logger.info("删除成功！")
        except Exception as e:
            logger.error("删除失败")
        h.recycleBin()

if __name__=="__main__":
    unittest.main(verbosity=2)