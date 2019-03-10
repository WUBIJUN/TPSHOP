from appium import webdriver


def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    # 设置可输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 不重置应用
    desired_caps['noReset'] = True
    # 定位吐司必传参数
    desired_caps['antomationName'] = 'Uiautomator2'
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # adb shell dumpsys window windows | findstr mFocusedApp
    # 包名启动名 com.tpshop.malls/.SPMainActivity
