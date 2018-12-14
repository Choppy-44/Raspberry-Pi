from flask import Flask
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

gpio.setmode(gpio.BCM)

gpio.setup(24,gpio.OUT)
gpio.setup(25,gpio.OUT)
gpio.setup(8,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.output(24,gpio.HIGH)
gpio.output(25,gpio.HIGH)
gpio.output(8,gpio.HIGH)
gpio.output(7,gpio.HIGH)

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello Choppy!"

@app.route("/pattern")

def pattern():
    
    gpio.output(24,gpio.LOW)
    gpio.output(25,gpio.LOW)
    gpio.output(8,gpio.LOW)
    gpio.output(7,gpio.LOW)

    time.sleep(1)

    gpio.output(24,gpio.HIGH)
    gpio.output(25,gpio.HIGH)
    gpio.output(8,gpio.HIGH)
    gpio.output(7,gpio.HIGH)


    time.sleep(1)
    return "4_On_Off Pattern has began execution!"
    

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 80,debug = True)
