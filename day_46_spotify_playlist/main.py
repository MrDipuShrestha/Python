import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ddc73ce201eb4478972b1607c984dfe8"
CLIENT_SECRET = "9bc981a7417447fc8b28102660370dab"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel? Write the date in the format of YYYY-MM-DD:")
url = "https://www.billboard.com/charts/hot-100/" + date
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Brave/1.50.114"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_name_spans = soup.find_all(name="h3", class_="c-title")
song_names = [song.getText() for song in song_name_spans]

song_uris = []
year = date.strip("-")[0]

for song in song_names:
    result = sp.search(q=f"Track:{song}, year:{year}", type='track')
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")