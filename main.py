from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class Reset:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_fb(self):
        self.driver.get("https://www.facebook.com")
        sleep(2)
        find_pop = self.driver.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]')
        find_pop.click()
        sleep(1)
        reset = self.driver.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[3]/a')
        reset.click()


test = Reset()
test.open_fb()

while True:
    pass
open_fb()