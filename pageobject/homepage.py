from pageobject.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger
import unittest

logger=Logger(logger="HomePage").getLog()
class HomePage(BasePage):
    ch_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')#左上角按钮
    regist_login_loc = (By.ID, "com.pdswp.su.smartcalendar:id/login")#点击登录或者注册
    regist_text_loc=(By.ID,"com.pdswp.su.smartcalendar:id/register")#注册一个吧
    userNmae_input_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    email_input_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    pwd_input_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    #注册按钮
    regist_btn_loc=(By.ID,"com.pdswp.su.smartcalendar:id/reguser")
    #点击已注册用户
    have_registr_loc=(By.ID,"com.pdswp.su.smartcalendar:id/title")

    #修改用户
    modify_loc=(By.ID,"com.pdswp.su.smartcalendar:id/imageView4")

    #备忘录
    addbwl_btn_loc=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    bwl_input_loc=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")
    #对勾
    quick_add_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    #加号添加备忘录
    menu_add_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")

    #搜索框
    search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")
    search_input_loc=(By.ID,"android:id/search_src_text")
    canale_loc=(By.XPATH,"//*[@text='取消']")

    #排序—应用设置
    design_loc=(By.XPATH,"//*[@text='应用设置']")
    order_bycolor_loc=(By.ID,'com.pdswp.su.smartcalendar:id/set_color')
    order_byoldtime_loc = (By.ID,'com.pdswp.su.smartcalendar:id/set_timesort')
    order_bynewtime_loc = (By.ID,'com.pdswp.su.smartcalendar:id/set_timesortnew')
    #排序长按
    long_order_loc=(By.ID,"com.pdswp.su.smartcalendar:id/sortBtn")
    long_text_loc=(By.XPATH,"//*[@text='排序']")
    duigou_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")

    #归档
    longpress_content_loc=(By.ID,'com.pdswp.su.smartcalendar:id/note_title')
    archive_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_archive")

    #查看归档记录
    check_archive_loc=(By.XPATH,"//*[@text='归档']")
    recovery_loc=(By.XPATH,"//*[@text='恢复']")

    #删除备忘录
    delete_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_delete")
    recycle_bin_loc=(By.XPATH,"//*[@text='回收站']")
    clear_all_loc=(By.ID,"com.pdswp.su.smartcalendar:id/button")
    sure_btn_loc=(By.XPATH,"//*[@text='确定']")

    #退出
    logout_btn_loc=(By.ID,"com.pdswp.su.smartcalendar:id/exit")

    def logout(self):
        self.click(*self.regist_login_loc)
        self.click(*self.logout_btn_loc)

    def registSuccess(self,username,email,pwd):
        self.click(*self.ch_loc)
        self.click(*self.regist_login_loc)
        self.click(*self.regist_text_loc)
        time.sleep(3)
        self.sendkeys(username, *self.userNmae_input_loc)
        self.sendkeys(email, *self.email_input_loc)
        self.sendkeys(pwd,*self.pwd_input_loc)
        time.sleep(2)
        self.click(*self.regist_btn_loc)
        self.click(*self.ch_loc)
        time.sleep(5)

    def registFail(self):
        pass

    def login(self,email,pwd):
        self.click(*self.ch_loc)
        self.click(*self.regist_login_loc)
        self.sendkeys(email,*self.email_input_loc)
        self.sendkeys(pwd,*self.pwd_input_loc)
        time.sleep(3)
        self.click(*self.regist_login_loc)
        self.click(*self.ch_loc)

    #断言判断用户名
    def alert_userName(self):
        user_name=self.getText(*self.userNmae_input_loc)
        return user_name


    def modify(self,content):
        self.click(*self.ch_loc)
        self.click(*self.regist_login_loc)
        self.click(*self.modify_loc)
        self.sendkeys(content,*self.userNmae_input_loc)
        self.click(*self.quick_add_loc)
        self.click(*self.ch_loc)
        self.click(*self.ch_loc)



    def bwl(self,content):
        self.click(*self.ch_loc)
        self.click(*self.addbwl_btn_loc)
        self.click(*self.bwl_input_loc)
        self.sendkeys(content,*self.bwl_input_loc)
        time.sleep(5)
        self.click(*self.quick_add_loc)


    def bwltwo(self,content):
        time.sleep(5)
        self.click(*self.menu_add_loc)
        self.click(*self.bwl_input_loc)
        self.sendkeys(content, *self.bwl_input_loc)
        time.sleep(3)
        self.click(*self.quick_add_loc)


    def search(self,content):
        self.click(*self.search_loc)
        self.sendkeys(content,*self.search_input_loc)
        self.keysend(66)
        self.click(*self.canale_loc)

    def order(self):
        self.logpress(*self.longpress_content_loc)
        self.click(*self.long_text_loc)
        self.swipe(660,138,660,552,5000)
        self.click(*self.duigou_loc)
        # 1[660,138][708,186]
        # 5[660, 522][708, 570]


    def archive(self):
        self.click(*self.ch_loc)
        self.click(*self.check_archive_loc)
        time.sleep(5)
        print(len(self.find_elements(*self.longpress_content_loc)))
        self.swipe(500,115,0,115,1500)
        time.sleep(2)
        logger.info("鼠标左滑成功")
        self.click(*self.recovery_loc)
        print(len(self.find_elements(*self.longpress_content_loc)))
        self.click(*self.ch_loc)

        # 文字[24,111][714,158] [0,110][24,206]
    def deletei(self):
        self.logpress(*self.longpress_content_loc)
        self.click(*self.delete_loc)

    def recycleBin(self):
        self.click(*self.ch_loc)
        self.click(*self.recycle_bin_loc)
        self.click(*self.clear_all_loc)
        self.click(*self.sure_btn_loc)
        self.click(*self.ch_loc)

    def alert_delete(self):
        length=len(self.find_elements(*self.longpress_content_loc))
        return length
































