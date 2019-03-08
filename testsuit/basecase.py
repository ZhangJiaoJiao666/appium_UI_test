import unittest
import warnings
from framework.appium_desired import startApp


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        self.driver=startApp()
        print("The test is starting")

    def tearDown(self):
        self.driver.quit()
        print("The testing is over")


if __name__=="__main__":
    unittest.main(verbosity=2)

