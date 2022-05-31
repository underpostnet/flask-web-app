

import os
import subprocess
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="estacionamiento"
)

print(mydb)

mycursor = mydb.cursor()

try:
  mycursor.execute("""
                      CREATE TABLE orden_estacionamiento (
                          id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                          patente VARCHAR(50),
                          hora_ingreso VARCHAR(50),
                          hora_salida VARCHAR(50),
                          estacionamiento INT(10),
                          cobro INT(10)
                      )
                  """
  )
  print("created table")
except:
  print("table already created")

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

class OrdenEstacionamiento:
    def __init__(self, patente, hora_ingreso, hora_salida, estacionamiento, cobro):
        self.patente = patente
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida
        self.estacionamiento = estacionamiento
        self.cobro = cobro

    def saveBD(self):
        sql = "INSERT INTO orden_estacionamiento (patente, hora_ingreso, hora_salida, estacionamiento, cobro) VALUES (%s, %s, %s, %s, %s)"
        val = (self.patente, self.hora_ingreso, self.hora_salida, self.estacionamiento, self.cobro)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


@app.route('/order_car', methods=['POST'])
def order_car():
    # request.method == 'POST'
    body = request.get_json()
    print('order_car', body)
    cobro = 0

    indexEst = int(body["estacionamiento"]) - 1;
    if dataEstacionamientos[indexEst]["estado"] == "disponible":
        if body["dias"] < 1:
            cobro = dataEstacionamientos[indexEst]["costo_auto"]
        elif body["dias"] < 30:
            cobro = dataEstacionamientos[indexEst]["costo_dia"]
        elif body["dias"] < 365:
            cobro = dataEstacionamientos[indexEst]["costo_mes"]
        else:
            cobro = dataEstacionamientos[indexEst]["costo_anio"]

        dataEstacionamientos[indexEst]["estado"] = "ocupado"

        orden = OrdenEstacionamiento(body["patente"], body["hora_ingreso"], body["hora_salida"], body["estacionamiento"], cobro)
        orden.saveBD()

        return 'true'

    return 'false'


@app.route('/parking_available', methods=['GET'])
def parking_available():
    available = []
    for est_ in dataEstacionamientos:
        if est_["estado"]=="disponible":
            available.append(est_["estacionamiento"])



    return json.dumps(available)

def readOrdenesEstacionamientos():
    print('readOrdenesEstacionamientos');
    mycursor.execute("SELECT * FROM orden_estacionamiento")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(type(x))
      print(x)


@app.route('/parkings', methods=['GET'])
def parkings():
    readOrdenesEstacionamientos()
    return 'true'
    # return json.dumps(available)

if __name__ == '__main__':
    app.run(port=dataEnv["port"], host=dataEnv["host"]) # debug=True
