from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from framework.logger import Logger
from framework.utils import Utils
import time
import os

logger=Logger(logger="BasePage").getLog()

class BasePage():
    def __init__(self,driver):
        self.driver=driver

    def clear(self,*loc):
        e1=self.find_element(*loc)
        try:
            e1.clear()
            logger.info("清除文本框中的内容:%s"+e1)
        except Exception as e:
            logger.error("未找到内容，清除失败%s"%e)
            self.get_windows_img()

    def click(self,*loc):
        e1=self.find_element(*loc)
        try:
            e1.click()
            logger.info("鼠标成功单击操作")
        except Exception as e:
            logger.error("未找到元素，鼠标单击失败%s",e)
            self.get_windows_img()

    def sendkeys(self,text,*loc):
        e1=self.find_element(*loc)
        try:
            e1.send_keys(text)
            logger.info("文本内容为："+e1.text)
            return e1
        except Exception as e:
            logger.error("未接收到任何文本",e)
            self.get_windows_img()

    def keysend(self,keycode):
        try:
            self.driver.keyevent(keycode)
            logger.info("键盘操作回车成功：")
        except Exception as e:
            logger.error("键盘操作失败%s"%e)
            self.get_windows_img()

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素" + loc)
        except Exception as e:
            logger.error("未找到页面元素",e)
            self.get_windows_img()

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_elements(*loc)
            logger.info("找到一组页面元素"+loc)
        except Exception as e:
            logger.error("未找到任何元素",e)
    def logpress(self,*loc):
        try:
            e1=self.find_element(*loc)
            TouchAction(self.driver).long_press(e1).perform()
            logger.info("长按成功")
        except Exception as e:
            logger.error("长按失败",e)
            self.get_windows_img()

    def getText(self,*loc):
        e1 = self.find_element(*loc)
        try:
            return  e1.text
            logger.info("找到的文本为：",e1.text)
        except Exception as e:
            logger.error("未找到文本%s"%e)
            self.get_windows_img()



    def get_excel(self,excel_path,sheetName):
        try:
            excel_list=Utils.read_excel(excel_path,sheetName)
            # list2=[excel_list[0].get("email"),excel_list[0].get("password")]
            return excel_list
            logger.info("获取数据表中的内容成功")
        except Exception as e:
            logger.error("获取失败%e"%e)
            self.get_windows_img()


    def swipe(self,x1,y1,x2,y2,t):
        try:
            self.driver.swipe(x1,y1,x2,y2,t)
            logger.info("成功从滑动")
        except Exception as e:
            logger.error("滑动失败")
            self.get_windows_img()

    def get_windows_img(self):
        '''
        在这里我们把file_path这个参数写死，直接保存到项目根目录的一个文件夹 \Screenrhots下
        :return:
        '''
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('截到图保存到文件夹/screenshots中  ')
        except Exception as e:
            logger.error('保存截图失败! %s' % e)
            self.get_windows_img()





