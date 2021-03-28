from flask import render_template, Flask, jsonify, redirect, request, url_for, send_file
import random
import string
import os
import pprint
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests
import json

song_ids = []

redirect_uri = 'http://localhost:8080/'
with open("credentials.json", "r") as file:
	credentials = json.load(file)
client_id = credentials['client_id']
client_secret = credentials['client_secret']

# client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))


def create_playlist(song_ids, room_id):
	scope = 'playlist-modify-public'
	auth_manager=SpotifyOAuth(scope=scope)
	spotipy.Spotify(auth_manager=auth_manager)
	playlist_name = room_id
	tracks = ["spotify:track:" + tid for tid in song_ids]
	response = sp.user_playlist_create(playlist_name, public=True, collaborative=False, description='')
	playlist_id = response["id"]
	sp.playlist_add_items(playlist_id, tracks, position=None)
	return playlist_id


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def load_app():

	if request.method == "GET":
		return render_template("home.html")

	if request.method == "POST":
		playlist_id = request.form["playlist_id"]
		results = sp.playlist(playlist_id)
		for item in results['tracks']['items']:
			track = item['track']['id']
			song_ids.append(track)
		#print(song_ids)
		# add list to db
		# comparing them with the other lists of song names
		# find 3 most similiar lists and their users
		room_id = ''.join(random.choice(string.ascii_lowercase) for x in range(30))
		return redirect(url_for("load_chatroom", room_id=room_id))


@app.route("/chatroom/<room_id>", methods=["GET", "POST"])
def load_chatroom(room_id):
	print(song_ids)
	print(room_id)
	playlist_id = create_playlist(song_ids, room_id)
	return render_template("chatroom.html", room_id=room_id, song_ids=song_ids, playlist_id=playlist_id)


def main():
	app.run(debug=True)


if __name__ == "__main__":
	main()
