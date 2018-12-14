from datetime import datetime

from time import sleep

mylog = open("log.txt","w")
i = 0
while i in range (5):
    data = str(datetime.now())
    mylog.write(data + "\n")
    print(data)
    sleep(1)
mylog.flush()
mylog.close()
