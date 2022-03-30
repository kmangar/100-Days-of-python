from bs4 import BeautifulSoup
import requests
import lxml


HEADERS = {"User-Agent": "Defined",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4"}

LINK = "https://www.amazon.com/dp/B08S3RHZ1Z/ref=cm_sw_em_r_mt_dp_BMPRX971Q6D6E6R0318Z?_encoding=UTF8&psc=1"

response = requests.get(LINK, headers=HEADERS)

website = response.text

soup = BeautifulSoup(website, "lxml")
price = soup.find(name="span", class_="a-offscreen").get_text()


print(f"${price}")




