from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 200
PROMISED_UP = 10
CHROME_DRIVER_PATH = "../Day48 Selenium/chromedriver.exe"
# email/ username / phone
TWITTER_EMAIL = "email"
TWITTER_PASSWORD = "password"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        print("getting internet speed..... ")
        # go to the speed test website
        self.driver.get("https://www.speedtest.net/")

        # find and click go
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()
        
        time.sleep(50)

        # re-initialize the up and down speed
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Up: {self.up}\nDown:{self.down}")

    def tweet_at_provider(self):
        print("tweeting at the provider...")

        # go to twitter
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        # login
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)

        time.sleep(3)

        password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        # wait 5sec and send out the tweet
        time.sleep(5)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 200down/10up")

        print("Tweet sent ")


twit_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twit_bot.get_internet_speed()
twit_bot.tweet_at_provider()























