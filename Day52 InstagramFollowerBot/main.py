import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../Day 48 Selenium/chromedriver.exe"

SIMILAR_ACCT = "username"
USERNAME = "username"
PASSWORD = "password"


class InstaFollwer():

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        print(f"Logging in as: {USERNAME}")
        
        # go to instagram 
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        # find and enter in username 
        username_box = self.driver.find_element(By.NAME, "username")
        username_box.click()
        username_box.send_keys(USERNAME)

        # enter the password
        password_box = self.driver.find_element(By.NAME, "password")
        password_box.click()
        password_box.send_keys(PASSWORD)

        # log in after username and passwords are entered
        time.sleep(2)
        password_box.send_keys(Keys.ENTER)
        print(f"logged in Successfully as {USERNAME}...\n\n")

    def find_followers(self):
        print(f"Finding followers from {SIMILAR_ACCT} account")
        # go to the account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCT}")

        # click on followers
        followers = self.driver.find_element(By.LINK_TEXT, "followers")
        followers.click()
        pass

    def follow(self):
        print(f"Initiating follow sequence")

        pass


bot = InstaFollwer(driver_path=CHROME_DRIVER_PATH)

bot.login()
bot.find_followers()
bot.follow()
