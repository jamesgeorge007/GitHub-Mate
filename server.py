
from flask import Flask, render_template, request, url_for, redirect
import requests
import json
import random

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/profile', methods = ['POST', 'GET'])

def profile():
    if request.method == 'POST':
        username = request.form['username']
        try:
            req = requests.get('https://api.github.com/users/' + username)
            if req.ok:
                github_data = json.loads(req.content)
                name = github_data['name']
                profile_pic = github_data['avatar_url']
                repos = github_data['public_repos']
                followers = github_data['followers']
                following = github_data['following']
                gists = github_data['public_gists']
                return render_template('profile.html', username = username, name = name, src = profile_pic, repos = repos, followers = followers, following = following, gists = gists)
            else:
                return render_template('profile.html', error = True)
        except:
            return render_template('connectionError.html')


if __name__ == '__main__':
    #print("Navigate to localhost:5000")
    app.run(debug = True)
