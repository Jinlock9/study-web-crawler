# test_4.py
# TEST Number 4 [Module : Web Testing Module]


# number 4.0 <selenium module>
# no. 4.0.0 : selenium module
# import selenium

# no. 4.0.1 : browser driver
# browser driver : browser 을 코드로 사용하기 위해 필요한 프로그램. crawler 와 web browser 을 연결시켜 주기 위한 프로그램.

# no. 4.0.2 : opening web browser
from selenium import webdriver

chrome_driver = webdriver.Chrome('ChromeDriver.exe')
# 다른 browser 들도 driver 설치 후 가능
'''
chrome_driver = webdriver.Chrome('ChromeDriver.exe')
iexplore_driver = webdriver.Ie('IEDriverServer.exe')
firefox_driver = webdriver.Firefox('FirefoxDriver.exe')
'''

# no 4.0.3 : wrongly state the web driver
# driver = webdriver.Ie('chromedriver.exe')  # error

# no 4.0.4 : not state the web driver
# driver = webdriver.Ie()
