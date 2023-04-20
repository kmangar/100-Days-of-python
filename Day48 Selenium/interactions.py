from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element_by_css_selector('#articlecount a')
# article_count.click()
# print(article_count.text)

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
fname = driver.find_element_by_name("fName")
fname.send_keys("Cam")

lname = driver.find_element_by_name("lName")
lname.send_keys("Mag")

email_add = driver.find_element_by_name("email")
email_add.send_keys("fakemail@mail.com")

email_add.send_keys(Keys.ENTER)








