
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import  datetime as dt

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pprint


URL="https://www.billboard.com/charts/hot-100/"
user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
header = {
    "user-agent": user_agent
}

dateformat= input("What year you would like to travel to?Please enter in YYYY-MM-DD format.")

response = requests.get(url=f"{URL}{dateformat}", headers=header).text

# soup= BeautifulSoup(response, "html.parser")
# #print(soup)
# song_title=soup.find_all(name="h3",  class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
soup = BeautifulSoup(response, 'html.parser')
song_names_spans = soup.select("li ul li h3")
#print(song_names_spans)
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id="e7c88f0655f94df1b409c829dbe0a3b9",
        client_secret="10c5a324fe494bf59a5fe2aeb0893d84",
        show_dialog=True,
        cache_path="token.txt",
        username="Little_Snekk18",
    )
)
user_id = sp.current_user()["id"]
print("User ID:", user_id)

year = dateformat.split("-")[0]
# song_names = ["The list of song", "titles from your", "web scrape"]
# print(year)
for song in song_names:

    result= sp.search(q=f'track:{song} year:{year}', type="track")
    pprint.pp(result)


# 2000-08-12