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

# find_all finds all the paragraphs
# all_anchor_tag = soup.find_all(name="p")
# # loops and prints the text in the tags
# for tag in all_anchor_tag:
#     print(tag.getText())

# find_all finds all a tags
# all_anchor_tag = soup.find_all(name="a")
# loops and prints all the href in the anchor tag
# for tag in all_anchor_tag:
#     # the get function gets specific item in the tag
#     print(tag.get("href"))










