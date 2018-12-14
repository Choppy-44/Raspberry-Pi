import urllib2
import datetime
import time
import RPi.GPIO as gpio
import smtplib
import Adafruit_DHT
from espeak import espeak

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


sensor =  Adafruit_DHT.DHT11  #_DHT11 GPIO SETUP
pin = 17

trig = 14   #_HCSR04 GPIO SETUP
echo = 15
switch = 26
gpio.setup(switch,gpio.IN,pull_up_down = gpio.PUD_DOWN)

ldr = 0    #_LDR SETUP
                       
server = smtplib.SMTP('smtp.gmail.com',587) #_THE SMTP ADDRESS AND SMTP PORT NUMBER OF GMAIL.
server.starttls()
            
url = 'http://thingspeak.com/update?key=R576HPKN9WNX5COM'  #_Project Key Installed

while True:

    #_____________________________________________________________SENSOR WORKING STARTED__________________________________________________________


    
    gpio.setup(trig,gpio.OUT)                                                                         #________________HCSR04 WORKING STARTED!!
    gpio.setup(echo,gpio.IN)

    gpio.output(trig,gpio.LOW)
    time.sleep(1)

    gpio.output(trig,gpio.HIGH)
    time.sleep(0.0001)

    gpio.output(trig,gpio.LOW)
    
    while(gpio.input(echo) == False):
        start = time.time()
    while (gpio.input(echo) == True):
        end = time.time()

    duration = end - start
    dist = duration * 17150
    dist = round(dist,2)

    if (dist<200 and dist>0):
        distance = dist

    print 'The Distance is ',distance                                                                 #________________HCSR04 WORKING SET!!



    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)                                        #________________DHT WORKING STARTED!!

    if humidity is not None and temperature is not None:
        print humidity
        print temperature                                                                             #________________DHT WORKING SET!!
        

    gpio.setup(4,gpio.OUT)                                                                            #________________LDR WORKING STARTED!!
    gpio.output(4,gpio.LOW)
    time.sleep(0.5)
    
    gpio.setup(4,gpio.IN)

    while(gpio.input(4) == False):
        ldr+=1

    print ldr

    ldr = 0                                                                                           #________________LDR WORKING SET!!

        

    #_____________________________________________________________SENSOR WORKING FINISHED__________________________________________________________


    #---------------------------------------------------------------------------------------------------------------------------------------------------------


    #___________________________________________________________________THINGSPEAK_________________________________________________________________


    myurl = url + '&field1=' + str(humidity) + '&field2=' + str(temperature) + '&field3=' + str(distance) + '&field4=' + str(ldr)
    response = urllib2.urlopen(myurl)
    print 'Thingspeak Request Response is ' + str(response.code)

    #___________________________________________________________________THINGSPEAK_________________________________________________________________


    #__________________________________________________________________SMTP MAILING________________________________________________________________

    server = smtplib.SMTP('smtp.gmail.com',587)                                                   #_THE SMTP ADDRESS AND SMTP PORT NUMBER OF GMAIL.
    server.starttls()

    print 'Sending the Mail...'

    server.login('actest344@gmail.com','@ChoppyPi3')

    tuday = datetime.datetime.today()
    mytime = datetime.datetime.now()
    
    mymsg = str('The Data Records of the Sensors as of '+str(tuday.year)+'-'+str(tuday.month)+'-'+str(tuday.day)+' '+str(mytime.hour)+'-'+str(mytime.minute)+'-'+str(mytime.second)+' are:\n'+'Humidity = '+str(humidity)+ '\nTemperature =  '+str(temperature)+'\nDistance = '+str(distance)+'\nLDR_Count = '+str(ldr) +'\nSent from my Raspberry Pi 3 using the SMTP Protocol!:)')
    print mymsg

    server.sendmail('actest344','tinkerac0@gmail.com',mymsg)
        
    server.quit()

    print 'Mail sent!'


    #__________________________________________________________________SMTP MAILING________________________________________________________________

        
    #_____________________________________________________________________eSPEAK___________________________________________________________________

        
    speech = str('\nThe Data Records of the Sensors are'+'\nHumidity = '+str(humidity)+ '\nTemperature =  '+str(temperature)+'\nDistance = '+str(distance)+'\nLDR_Count = '+str(ldr))
    print(speech)

    time.sleep(0.55) #To ensure a gap between the visual and the switch press.
    
    if (gpio.input(switch)== True):
        espeak.synth(speech)

    time.sleep(5) #To ensure a delay between the audio output and the next reading.


    #_____________________________________________________________________eSPEAK___________________________________________________________________
            
        
            

            
