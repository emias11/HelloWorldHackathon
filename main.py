import json
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests

# client_id = '' #insert your client id
# client_secret = '' # insert your client secret id here

redirect_uri = 'http://localhost:8080/'

# client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

# print(current_user_playlists(limit=50, offset=0))

# GET https://api.spotify.com/v1/users/{'staplegun.'}/playlists

playlists = sp.user_playlists('staplegun.')

playlist_list = []
for playlist in playlists['items']:
	playlist_list.append(playlist)

results = sp.playlist(playlist_list[1])

song_ids = []
for item in results['tracks']['items']:
	track = item['track']['id']
	song_ids.append(track)

print(song_ids)


