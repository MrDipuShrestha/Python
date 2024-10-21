from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movies_tag = soup.find_all(name="h3", class_="title")

movies_list = [movies.getText() for movies in movies_tag]

all_movies = movies_list[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")

print(soup)