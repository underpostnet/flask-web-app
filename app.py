

import os
import subprocess

from underpost_modules import view
from flask import Flask


print('run path: ', os.getcwd())

# os.path.isfile
if not os.path.isdir('./underpost-library'):
    p = subprocess.run("git clone https://github.com/underpostnet/underpost-library")
else:
    os.chdir('./underpost-library')
    p = subprocess.run("git pull origin master")
    os.chdir('..')


# view.render()


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
