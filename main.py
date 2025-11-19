import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import datetime as dt
import pprint


URL="https://www.billboard.com/charts/hot-100/"
user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
header = {
    "user-agent": user_agent
}

dateformat= input("What year you would like to travel to?Please enter in YYYY-MM-DD format.")
response = requests.get(url=f"{URL}{dateformat}", headers=header).text

soup = BeautifulSoup(response, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#----------spotify------------------
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
print(sp.current_user())
user_id = sp.current_user()["id"]
print("User ID:", user_id)

now = dt.datetime.now()
year = now.year
song_uris=[]
print(year)

for song in song_names:
    result = sp.search(q=f'spotify:track:{song} year:{year}', type="track")
    #pprint.pp(f"{result} \n -----------------------")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        #print(uri)
        song_uris.append(uri)
    except:
        print(f"{song} not available")


#------------------------------Creating and Adding to Spotify Playlist----------------------------------
name_of_playlist = f"{dateformat} Billboard 100"

playlist =sp.user_playlist_create(user=user_id, name=name_of_playlist, public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris, position=None)

#sp.user_playlist_add_tracks(user=user_id, playlist_id=song_uris, tracks=user_id, position=None)
print("------------COMPLETE-----------------")



# 2000-08-12