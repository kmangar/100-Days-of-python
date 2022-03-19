from bs4 import BeautifulSoup
import lxml

with open("//Users/kham/document/udemy/python 100/100-Days-of-python/Day41-44/44/index.html") as file:
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

# getting specific item using find below finds h1 and id called name
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_p = soup.find(name="p", class_="intro")
# print(section_p.getText())

# select get all item that matches the prams
# soup.select()
# select_one will only get the first item it matches
# soup.select_one()


connect_link = soup.select(selector="div .footer-link ")
print(connect_link)








