import urllib2
import datetime
import time
import RPi.GPIO as gpio
import smtplib
import Adafruit_DHT

server = smtplib.SMTP('smtp.gmail.com',587) #_THE SMTP ADDRESS AND SMTP PORT NUMBER OF GMAIL.
server.starttls()

sensor =  Adafruit_DHT.DHT11
pin = 17
                       
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
            
url = 'http://thingspeak.com/update?key=GFM3RV5ONCXID580'

while True:
    server = smtplib.SMTP('smtp.gmail.com',587) #_THE SMTP ADDRESS AND SMTP PORT NUMBER OF GMAIL.
    server.starttls()

    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)

    if humidity is not None and temperature is not None:
        print humidity
        print temperature

        myurl = url + '&field1=' + str(humidity) + '&field2=' + str(temperature)
        response = urllib2.urlopen(myurl)

        print 'Sending the Mail...'

        server.login('actest344@gmail.com','@ChoppyPi3')

        tuday = datetime.datetime.today()
        mytime = datetime.datetime.now()
    
        mymsg = str('The Humidity & the Temperature of the room as of '+str(tuday.year)+'-'+str(tuday.month)+'-'+str(tuday.day)+' '+str(mytime.hour)+'-'+str(mytime.minute)+'-'+str(mytime.second)+' are '+str(humidity) + ' & '+str(temperature) + ' respectively.' + '\n' +'Sent from my Raspberry Pi 3 using the SMTP Protocol!:)')
        print mymsg

        sarde = str ('\n10 la 2.. 10 la 2.. 10 la 2 SARDE,SARDE,SARDE,SARDE,SARDE!!!')

        server.sendmail('actest344','abolishastri@gmail.com',mymsg+sarde)
        server.sendmail('actest344','shitalk8184@gmail.com',mymsg+sarde)
        server.sendmail('actest344','tanvigupte.13@gmail.com',mymsg)
        server.sendmail('actest344','ritusarwade@gmail.com',mymsg+sarde)
        
        server.quit()

        print 'Mails sent!'

        time.sleep(15)
