import os
import time
import datetime
from log_write_to_text_file import log_write_to_text_file


def measure_temperature():
        while True:
                temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
                temp = (temp.replace("temp=",""))
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(now, temp)
                log_write_to_text_file('temp: {0}'.format(temp))
                time.sleep(1)



if __name__ == '__main__':
    measure_temperature()
