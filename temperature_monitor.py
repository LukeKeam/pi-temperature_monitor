import os
import time
import datetime
from log_write_to_text_file import log_write_to_text_file


def measure_temperature():
        while True:
                temperature = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
                temperature = (temperature.replace("temp=",""))
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(now, temperature)
                log_write_to_text_file('temp: {0}'.format(temperature))
                time.sleep(1)



if __name__ == '__main__':
    measure_temperature()
