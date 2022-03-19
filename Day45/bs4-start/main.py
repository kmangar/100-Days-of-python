from bs4 import BeautifulSoup
import lxml

with open("/Users/kham/document/udemy/python 100/100-Days-of-python/Day41-44/HTML-Personal Site/index.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

# prints the title
# print(soup.title)

# the .string prints the content on the tag
# print(soup.title.string)

# prettify indents the contents
# print(soup.prettify())

# prints the first paragraph
# print(soup.p)









