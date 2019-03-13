from flask import Flask, render_template, request, url_for, redirect
from github import Github, UnknownObjectException
from requests.exceptions import ConnectionError
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    if request.method == 'POST':
        username = request.form['username']
        try:
            user = Github().get_user(username)
            return render_template('profile.html', user=user)
        except UnknownObjectException:
            return render_template('profile.html', error=True)
        except ConnectionError:
            return render_template('connectionError.html')
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
