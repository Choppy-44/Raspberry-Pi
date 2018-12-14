import bluetooth                                                #__importing the bluetooth library for python to be able to access the BLE of Pi 
import RPi.GPIO as gpio                                         #__calling for header file which helps in using GPIOs of PI
import time                                                     #__importing the time library to use time related operations such as delays  
import Adafruit_DHT                                             #__importing Adafruit's library to access the methods that help obtaining the temperature 
from espeak import espeak                                       #__importing the voice synthesis module for the Pi to generate audio output of the desired strings

sensor =  Adafruit_DHT.DHT11                                    #__declaring the DHT sensor(11 or 22)
pin = 2                                                         #__gpio to DHT11 connection is declared here
                       
gpio.setwarnings(False)                                         #__to avoid Warnings on the IDLE console
gpio.setmode(gpio.BCM)                                          #__Declaration of the gpio numbering method(BOARD or BCM)

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )     #__Setting the bluetooth Communication Protocol
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)                                         #__For Pi to be online to communicate
 
client_socket,address = server_socket.accept()                  #__Accepting the Client address
print "Accepted connection from ",address                       #__Address printing on console
time.sleep(2.5)                                                 #__Delay
conn = 'Device Online'                           
espeak.synth(conn)                                              #__Audio Out to know that the communication has been established

while True:
    data = client_socket.recv(1024)                             #__Accept string data input of Voice command from the Phone
    print "Received: %s" % data
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)  #__Obtain Temperature Reading of the Environment from the DHT

    #__The following if loop checks if the temp readings are non zero & if the voice inputin the data variable matches the following strings
    #__If the 2 conditions are satisfied then the Pi will generate an Audio output notifying the temperature of the Environment
    
    if (((humidity is not None) and (temperature is not None)) and (data == 'temperature' or data == 'temp' or data == 'what is the temperature' or data == 'what is the temperature of the room')):  
        print temperature
        print humidity
        spTemp = 'The temperature of the room is {}'.format(temperature)
            
        espeak.synth(spTemp)

    if data == 'QUIT' or data == 'Quit' or data == 'quit':                      #__If voice input string matches QUIT then the program breaks out of infinite while loop      
        break
    
 
client_socket.close()                                           #__Close Client Connection
server_socket.close()                                           #__Close Server Connection
