from datetime import datetime

from time import sleep

log = open("log.txt","w")
i = 0
for i in range (5):
    data = str(datetime.now())
    log.write(data + "\n")
    print(data)
    sleep(1)
    log.flush()
log.close()
