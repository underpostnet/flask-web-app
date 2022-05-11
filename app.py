

import os
from underpost_modules import view

import subprocess

print('run path: ', os.getcwd())

# os.path.isfile
if not os.path.isdir('./underpost-library'):
    p = subprocess.run("git clone https://github.com/underpostnet/underpost-library")
else:
    os.chdir('./underpost-library')
    p = subprocess.run("git pull origin master")
    os.chdir('..')





view.render()
