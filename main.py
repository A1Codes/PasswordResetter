from selenium import webdriver
from time import sleep

from accounts import facebook, instagram
from selenium.webdriver.common.keys import Keys


class Reset:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.open_fb()
        self.open_insta()

    def open_fb(self):
        self.driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
        sleep(5)
        self.driver.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
        sleep(1)
        input_field = self.driver.find_element('xpath',
                                               '/html/body/div[1]/div[1]/div[1]/div/div/div/form/div/div[2]/div/table/tbody/tr[2]/td[2]/input')
        input_field.send_keys(facebook)
        self.driver.find_element('xpath',
                                 '/html/body/div[1]/div[1]/div[1]/div/div/div/form/div/div[3]/div/div[1]/button').click()

    def open_insta(self):
        self.driver.get("https://www.instagram.com/accounts/password/reset/")
        sleep(5)
        self.driver.find_element('xpath',
                                 '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
        input_field = self.driver.find_element('xpath',
                                               '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[4]/form/label/input')
        sleep(1)
        input_field.send_keys(instagram)
        sleep(3)
        input_field.send_keys(Keys.ENTER)


Reset()

while True:
    pass
Reset()
