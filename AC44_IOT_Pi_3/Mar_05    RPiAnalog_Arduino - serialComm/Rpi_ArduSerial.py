import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
print('Serial Port open')         # check which port was really used

while True:
    a = ser.readline()
    b = a.split(',')
    print a
    
    
#ser.write(b'hello')     # write a string
#ser.close()     
