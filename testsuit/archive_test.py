from testsuit.basecase import BaseTestCase
from pageobject.homepage import HomePage
import unittest


class ArchiveTest(BaseTestCase):
    def test_archive(self):
        """归档与恢复功能"""
        h=HomePage(self.driver)
        h.archive()

if __name__=="__main__":
    unittest.main(verbosity=2)
