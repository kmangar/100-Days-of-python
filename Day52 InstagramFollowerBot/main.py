import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "../Day 48 Selenium/chromedriver.exe"

SIMILAR_ACCT = input("similar account to look up: ")
USERNAME = input("Enter your username: ")
PASSWORD = input("Enter your password: ")


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
        time.sleep(6)
        print(f"logged in Successfully as {USERNAME}...\n\n")

    def find_followers(self):
        print(f"Finding followers from {SIMILAR_ACCT} account")
        # go to the account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCT}")
        time.sleep(2)

        # click on followers
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup)
            # element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        print(f"Initiating follow sequence")
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollwer(driver_path=CHROME_DRIVER_PATH)

bot.login()
bot.find_followers()
bot.follow()
