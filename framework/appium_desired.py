import yaml
from appium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getLog()

def startApp():
    desired_caps={}
    with open('../config/bwl.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps["platformName"]=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['sessionOverride']=data['sessionOverride']

    desired_caps['app']=data['app']
    desired_caps['noReset']=['noReset']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    # driver=webdriver.Remote('http://'+str(data['ip']) + ':' +str(data['port'])+'/wd/hub',desired_caps)
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    return driver


if __name__=="__main__":
    startApp()



