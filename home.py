from flask import render_template, Flask, jsonify, redirect, request, url_for, send_file
import uuid

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def load_app():
	if request.method == "GET":
		return render_template("home.html")

	if request.method =="POST":
		playlist_id = request.form["playlist_id"]
		# logic for retrieving song names from the playlist
		# add list to db
		# comparing them with the other lists of song names
		# find 3 most similiar lists and their users
		room_id = uuid.uuid4()
		print(playlist_id)
		return redirect(url_for("load_chatroom", room_id=room_id))

@app.route("/chatroom/<room_id>", methods=["GET", "POST"])
def load_chatroom(room_id):
	return render_template("chatroom.html")


def main():
	app.run(debug=True)


if __name__ == "__main__":
	main()