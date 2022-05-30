

import os
import subprocess
import json

# from [first level folder] import [py script file name]

from flask import Flask, send_from_directory, render_template, request


print('run path: ', os.getcwd())


with open('./data/paths.json') as f:
    dataPaths = json.load(f)

with open('./data/env.json') as f:
    dataEnv = json.load(f)

with open('./data/estacionamientos.json') as f:
    dataEstacionamientos = json.load(f)

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


app = Flask(__name__, template_folder='templates')


# vistas
for dataView in dataPaths:
    @app.route(dataView["uri"])
    def renderView():
        return render_template('index.html',
        uri = dataView["uri"],
        title = dataView["title"],
        description = dataView["description"],
        router = dataView["router"],
        lang = dataView["lang"],
        charset = dataEnv["charset"] )



# estaticos
@app.route('/<path:path>')
def static_file(path):
    print("static_file", path)
    return send_from_directory(directory = 'client', path = path) # as_attachment=True


# api

# class OrdenEstacionamiento:
#     def __init__(self):





@app.route('/order_car', methods=['POST'])
def order_car():
    # request.method == 'POST'
    body = request.get_json()
    print('order_car', body)

    indexEst = int(body["estacionamiento"]) - 1;
    if dataEstacionamientos[indexEst]["estado"] == "disponible":
       print('valid')
    return 'true'




@app.route('/parking_available', methods=['GET'])
def parking_available():
    available = []
    for est_ in dataEstacionamientos:
        if est_["estado"]=="disponible":
            available.append(est_["estacionamiento"])



    return json.dumps(available)

if __name__ == '__main__':
    app.run(port=dataEnv["port"], host=dataEnv["host"]) # debug=True
