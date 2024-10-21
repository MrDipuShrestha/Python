from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
all_web_content = response.text

soup = BeautifulSoup(all_web_content, "html.parser")
response_tag = soup.find_all("a ")

print(response_tag)
































# from bs4 import BeautifulSoup
#
# with open("website.html", 'r', encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_a_tags = soup.find_all(name='a')
#
# for tag in all_a_tags:
#     print(tag.getText())
#
# one = soup.h3["class"]
# print(one)
#
# two = soup.select_one("h3.heading")
# print(two)
