from flask import Flask, render_template, request, redirect
import requests
from io import FileIO
from random import choice
from string import ascii_letters as letters, digits
from hashlib import sha256
import base64
import sqlite3

client_secret = FileIO("priv/client_secret").readline().decode("ascii")
client_id = FileIO("priv/client_id").readline().decode("ascii")

app = Flask(__name__, template_folder=".")


@app.route("/")
def index():
  print(database)
  return render_template('templates/messages.html')

@app.route("/messaging",methods=['POST'])
def handle_msg():
  sender = request.cookies
  print(sender)
  return redirect("/")

challenge = ""
verifier = ""
redirect_uri = "http://localhost:5000/register/complete"

@app.route("/register")
def register_user():
  global challenge
  global verifier
  verifier = ''.join(choice(letters+digits) for _ in range(16))
  challenge = base64.b64encode(sha256(verifier.encode("utf-8")).digest())
  print(verifier,challenge)
  url = "https://accounts.spotify.com/en/authorize?client_id={}&response_type=code&redirect_uri={}&code_challenge_method=S256&code_challenge={}".format(client_id,redirect_uri,challenge)
  return redirect(url)

def get_token_from_code(code):
  token = requests.post("https://accounts.spotify.com/api/token",
                        {'client_id':client_id,'grant_type':'authorization_code','code':code,'redirect_uri':redirect_uri,'code_verifier':verifier})
  print(token.text)
  return token

@app.route("/register/complete")
def complete_reg():
  #try:
    code = request.values["code"]
    print(verifier,challenge)
    print(code)
    token = get_token_from_code(code)
    # user_id = requests.get("https://api.spotify.com/v1/me",
    #                        {'Authorization':'Bearer {}'.format(token),
    #                         'Accept':'application/json',
    #                         'Content-Type':'application/json',
    #                         'client_id':client_id,'client_secret':client_secret})
    # print(user_id.text)
    #database = sqlite3.connect("priv/database.db").execute("SELECT * from USERS").fetchall()
    return redirect("/")
  #except:
  #  return redirect("/register/fail")

if __name__ == "__main__":
  app.run(debug=True)