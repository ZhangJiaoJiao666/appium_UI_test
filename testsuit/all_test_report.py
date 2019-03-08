import HTMLTestRunner
from testsuit.addbwl_test import AddbwlTest
from testsuit.archive_test import ArchiveTest
from testsuit.order_test import OrderTest
from testsuit.login_test1 import LoginTest
from testsuit.delete_test import DeleteTest
from testsuit.modify_test import ModifyTest
from testsuit.regist_test import RegistTest
from testsuit.search_test import SerchTest
import unittest
import os
import time

new_path=os.path.dirname(os.path.realpath("."))
report_path=os.path.join(new_path+'\Report')
if not os.path.exists(report_path):
    os.makedirs(report_path)
# print(new_path)
# print(report_path)
suite=unittest.TestSuite()
suite.addTests(unittest.makeSuite(AddbwlTest))
suite.addTests(unittest.makeSuite(SerchTest))
suite.addTests(unittest.makeSuite(OrderTest))
suite.addTests(unittest.makeSuite(ArchiveTest))
suite.addTests(unittest.makeSuite(DeleteTest))
suite.addTests(unittest.makeSuite(RegistTest))
suite.addTests(unittest.makeSuite(ModifyTest))
suite.addTests(unittest.makeSuite(LoginTest))



if __name__=="__main__":
    html_report=report_path + r'\result.html'
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="测试报告",description="手机端测试报告情况描述")
    runner.run(suite)
