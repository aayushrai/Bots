from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Whatsapp:

    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        time.sleep(2)
    def get_title(self):
        driver = self.driver
        time.sleep(2)
        span = driver.find_elements_by_class_name("_19RFN")
        titles=[ele.get_attribute("title") for ele in span]
        return titles
    def choose_user(self):
        driver = self.driver
        users = self.get_title()
        for id,name in enumerate(users):
            print(str(id) + " : " + str(name))
        selected_user = int(input())
        driver.find_element_by_xpath('//*[@title="{}"]'.format(str(users[selected_user]))).click()
        
# How to handle windows file upload using Selenium WebDriver?

aayush = Whatsapp()
aayush.login()
aayush.choose_user()
