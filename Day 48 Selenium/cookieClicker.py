from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# cookies = driver.find_element_by_id("cookies")
#
# upgrades = driver.find_elements_by_css_selector(".content .price")
# events = {}
#
# timeout = time.time() + 60*5
#
# for n in range(len(upgrades)):
#     events[n] = {
#         "price": upgrades[n].text,
#         "name": upgrades[n].id
#     }
# print(events)
#
# while True:
#     cookies.click()
#     test = 0
#     if test == 5 or time.time() > timeout:
#         break
#     test = test - 1
#
#

timeout = time.time() + 5
game_time = time.time() + 60 * 5  # 5minutes break

cookie = driver.find_element(
    By.ID, "cookie"
)

while True:
    cookie.click()
    if time.time() > timeout:
        # Check for best item, class '', i.e not 'grayed'
        items_to_buy = driver.find_elements(
            By.CSS_SELECTOR, 'div[class=""] b'
        )
        buy = items_to_buy[:][-1].click() # Buy last item in list, aka most expensive
        timeout = time.time() + 5

    if time.time() > game_time:
        speed = driver.find_element(
            By.ID, "cps").text
        print(speed)
        break