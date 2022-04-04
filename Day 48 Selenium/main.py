from selenium import webdriver


chrome_driver_path = "P:\Program\webdriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.google.com")

# close will only close the current tab
# driver.close()

# will close the application
# driver.quit()

# find by ID 
# price = driver.find_element_by_id("priceblock-ourprice")
# print(price.text)

# find by element name 
# search_bar = driver.find_element_by_name("q")

# find element by class name 
# logo = driver.find_element_by_class_name("python-logo")

# find by css selector 
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a") 

# find by xpath 
# bug_link = driver.find_element_by_xpath('//*[@id="question-dialog"]/a/span')
