import time

def logit(message):
    with open('/home/pi/Desktop/AFKZenCoders/PS12/Logs.txt', 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()
        