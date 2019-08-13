from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class instabot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elemnt = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elemnt.clear()
        user_name_elemnt.send_keys(self.username)
        password_elemnt = driver.find_element_by_xpath("//input[@name='password']")
        password_elemnt.clear()
        password_elemnt.send_keys(self.password)
        password_elemnt.send_keys(Keys.RETURN)

    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag +"/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script(("window.scrollTo(0,document.body.scrollHeight);"))
            time.sleep(2)
        elements = driver.find_elements_by_tag_name('a')
        hrefs = [elem.get_attribute('href') for elem in elements]
        href_pic = [href for href in hrefs if hashtag in href]
        print(hashtag + " photo " +str(len(href_pic)))


aayush = instabot("marvelandpubg","Marvel#21")
aayush.login()
aayush.like_photo("newyork")