import RPi.GPIO as gpio
import time
import datetime

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(18,gpio.OUT)

while True:
    
    tuday = datetime.datetime.today()
    mytime = datetime.datetime.now()    

    fromadd = 'actest344@gmail.com'
    toadd = 'tinkerac0@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = 'Buzzer Reporting!'

    body = 'The buzzer was awake on '+str(tuday.year)+'-'+str(tuday.month)+'-'+str(tuday.day)+' at '+str(mytime.hour)+'-'+str(mytime.minute)+'-'+str(mytime.second)
    msg.attach(MIMEText(body,'plain'))
    

    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.starttls()
    server.login('actest344','@ChoppyPi3')
    

    gpio.output(18,gpio.HIGH)
    time.sleep(2.5)
    gpio.output(18,gpio.LOW)
    time.sleep(0.5)
    gpio.output(18,gpio.HIGH)
    time.sleep(2.5)
    gpio.output(18,gpio.LOW)
    time.sleep(0.5)

    text = msg.as_string()

    server.sendmail('actest344','tinkerac0@gmail.com',text)
    server.quit()
    print 'Mail Sent!'

    time.sleep(3)

    
