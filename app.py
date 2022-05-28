

import os
import subprocess
import json

from underpost_modules import view
from flask import Flask, send_from_directory, render_template, request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# <h3>{{ utc_dt }}</h3>
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
# render_template('index.html', utc_dt=datetime.datetime.utcnow())


print('run path: ', os.getcwd())


with open('./data/paths.json') as f:
    dataPaths = json.load(f)

with open('./data/env.json') as f:
    dataEnv = json.load(f)

# os.path.isfile
if not os.path.isdir('./client/underpost-library'):
    os.chdir('client')
    p = subprocess.run("git clone https://github.com/underpostnet/underpost-library")
    os.chdir('..')
else:
    os.chdir('./client/underpost-library')
    p = subprocess.run("git pull origin master")
    os.chdir('../..')


# view.render()


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/<path:path>')
def static_file(path):
    print("static_file", path)
    return send_from_directory(directory = 'client', path = path) # as_attachment=True


if __name__ == '__main__':
    app.run(port=dataEnv["port"], host=dataEnv["host"]) # debug=True
