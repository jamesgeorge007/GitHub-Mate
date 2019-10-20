from gmate import app
from flask import render_template, request, url_for, redirect
from github import Github, UnknownObjectException
from requests.exceptions import ConnectionError
import requests


@app.route('/')
def index():
    return render_template('index.html',InvalidUserName=False)


@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    username=request.form['username']
    response = requests.get("https://api.github.com/users/"+username)
    if(response.status_code != 200):
        return render_template('index.html',InvalidUserName=True)
    else:
        response = response.json()
        name = response['name'];
        picture = response['avatar_url']
        bio = response['bio']
        followers = response['followers']
        following = response['following']
        email = response['email']
        blog = response['blog']
        open_repos = response['public_repos']
        return render_template('profile.html',name=name,bio=bio,
        avatar=picture,following=following,followers=followers,
        open_repos = open_repos,blog=blog,email=email,InvalidUserName=False)
