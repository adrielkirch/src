from datetime import datetime

def now():
    now = datetime.now()
    return now.strftime("%d-%m-%y %H:%M:%S")

def today():
    str = now()
    str = str[0:8]
    return str
