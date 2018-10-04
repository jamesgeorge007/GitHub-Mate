
from flask import Flask, render_template, request, url_for, redirect
import requests
import json

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
                print(github_data)
                repo_url = requests.get(github_data.get('repos_url'))
                repo_url = repo_url.json()
                repos_with_issues = {}
                for repo in repo_url:
                    print(repo)
                    open_issues = repo.get('open_issues')
                    if open_issues > 0:
                        repos_with_issues[repo.get('html_url')] = open_issues
                print(repos_with_issues)
                name = github_data['name']
                profile_pic = github_data['avatar_url']
                repos = github_data['public_repos']
                followers = github_data['followers']
                following = github_data['following']
                gists = github_data['public_gists']
                return render_template('profile.html', username=username, name=name, src=profile_pic, repos=repos, followers=followers, following=following, gists=gists, repos_with_issues=repos_with_issues)
            else:
                return render_template('profile.html', error=True)
        except:
            return render_template('connectionError.html')


if __name__ == '__main__':
    #print("Navigate to localhost:5000")
    app.run(debug = True)
