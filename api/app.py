
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, url_for, redirect

from discoauth import auth, discord

import os


app = Flask(__name__)

CLID = os.getenv('CLID')
CLSEC = os.getenv('CLSEC')
reuri = "https://www.chronicbot.xyz/callback"
scope = ["identify", "guilds"]

url = auth(CLID, scope, reuri).url()


@app.route('/')
def index():
    return render_template("main_page.html")

@app.route('/login')
def login():
    return redirect(url)

@app.route('/callback')
def callback():
    session["code"] = request.args.get("code")
    return redirect(url_for("dash"))

@app.route('/dashboard')
def dash():
    api = discord(CLID, CLSEC, scope, reuri)
    if "token" not in session:
        if "code" not in session:
            return redirect(url_for("login"))
        r = api.token(session["code"])
        session["token"] = r["access_token"]
    user = api.user(session.get("token")).fetch()
    id = user['id']
    avatar_hash = user['avatar']
    avatar_url = f"https://cdn.discordapp.com/avatars/{id}/{avatar_hash}"
    guilds = api.user(session.get("token")).guilds()
    x = 0
    guildLList = []
    guildList = []
    for guild in guilds:
        guildList.append(guild)
        x += 1
        if x == 5:
            guildLList.append(guildList)
            guildList = []
            x = 0
    return render_template("auth.html", user_avatar=avatar_url, user=user, guildLList=guildLList)

