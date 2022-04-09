import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
job_url = "https://www.linkedin.com/jobs/search/?currentJobId=2917056993&distance=25&f_E=2&f_F=it&f_PP=102771607" \
          "%2C104944236%2C103764036%2C101233134%2C102061174%2C107018819%2C107121028&f_WT=1" \
          "&geoId=102771607&location=Louisville%2C%20Kentucky%2C%20United%20States&sortBy=R"


username = "youremail@gmail.com"
password = "your-password"

driver.get(job_url)


# login
login = driver.find_element(
    By.LINK_TEXT, "Sign in"
)

login.click()

# find input box to input user data to login
username_input = driver.find_element(
    By.ID, "username"
)
username_input.send_keys(username)

paswd_input = driver.find_element(
    By.ID, "password"
)

# input username and password to login
paswd_input.send_keys(password)
paswd_input.send_keys(Keys.ENTER)


job_list = driver.find_elements(
    By.CLASS_NAME, "jobs-search-results__list-item" )
print(len(job_list))

chat_min = driver.find_element(
    By.CLASS_NAME, "msg-overlay-bubble-header__details")

chat_min.click()

# go through the jobs and saves & follow the company
for index in range(25):
    job_list = driver.find_elements(
        By.CLASS_NAME, "jobs-search-results__list-item")

    job = job_list[index]
    job.click()
    time.sleep(1)
    save = driver.find_element(
        By.CLASS_NAME, "jobs-save-button")
    save.click()

    try:
        follow = driver.find_element(
            By.CLASS_NAME, "follow")
        follow.click()

    except NoSuchElementException:
        pass


driver.quit()


