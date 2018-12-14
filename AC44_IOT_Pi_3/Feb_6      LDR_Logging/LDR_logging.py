import RPi.GPIO as gpio
import time
import datetime

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

count = 0

a = open('/home/pi/AC44_IOT_Pi_3/Feb_6/ldrlog.csv','a')
a.write("Light,Year,Month,Day,Hours,Minutes,Seconds,Timestamp\n")
while True:
    gpio.setup(4,gpio.OUT)
    gpio.output(4,gpio.LOW)
    time.sleep(0.5)

    gpio.setup(4,gpio.IN)

    while(gpio.input(4) == False):
        count+=1

    tuday = datetime.datetime.today()
    mytime = datetime.datetime.now()
    ticks = time.time()
    
    print count
    
    data = str(count)+','+str(tuday.year)+','+str(tuday.month)+','+str(tuday.day)+','+str(mytime.hour)+','+str(mytime.minute)+','+str(mytime.second)+','+str(ticks)+'\n' 
    print (data)

    a = open('/home/pi/AC44_IOT_Pi_3/Feb_6/ldrlog.csv','a')
    a.write(data)

    count = 0
    time.sleep(1)

    a.flush()
    a.close()
