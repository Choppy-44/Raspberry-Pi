import Adafruit_BMP.BMP085 as BMP085
from time import sleep
from flask import Flask,render_template
import datetime

sensor = BMP085.BMP085()

app = Flask(__name__)
@app.route("/")

def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    temp = sensor.read_temperature()
    prs = sensor.read_pressure()
    alt = round(sensor.read_altitude(),2)
    slprs = sensor.read_sealevel_pressure()
    templateData = {
        'title': 'Hello',
        'time': timeString,
        'temp': temp,
        'prs' : prs,
        'alt' : alt,
        'slprs' : slprs
        }
    return render_template('BMP180.html',**templateData)


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 80,debug = True)
    
while True:
    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
    sleep(1)



