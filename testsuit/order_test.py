from pageobject.homepage import HomePage
from testsuit.basecase import BaseTestCase
import unittest

class OrderTest(BaseTestCase):
    def test_order(self):
        """排序功能"""
        h=HomePage(self.driver)
        h.order()
if __name__=="__main__":
    unittest.main(verbosity=2)