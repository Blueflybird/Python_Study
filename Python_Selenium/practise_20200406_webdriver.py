# selenium 实现网页自动化

from selenium import webdriver

driver=webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe')
# driver=webdriver.chrome('C:\Users\Admin\Downloads\chromedriver_win32')
# driver.fullscreen_windows()
driver.get('http://amazon.com')
driver.find_element_by_id("s-suggestion").click()
