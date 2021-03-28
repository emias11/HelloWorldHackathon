from flask import Flask, render_template, request, redirect
import requests
import sqlite3
from io import FileIO

client_secret = FileIO("priv/client_secret").readline
client_secret = FileIO("priv/client_token").readline
app = Flask(__name__, template_folder=".")

me=1234
new_var = 43121224
messages = [(me,"hello")(34,"hello! I'm another person"),(35,"Hello other person!")]

@app.route("/")
def index():
  return render_template('templates/messages.html')

@app.route("/messaging",methods=['POST'])
def handle_msg():
  sender = request.cookies
  messages.append(())
  return redirect("/")

@app.route("/register")
def register_user():
  redirect("https://")



if __name__ == "__main__":
  app.run(debug=True)