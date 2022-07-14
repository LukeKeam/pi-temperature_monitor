# link
https://techgeek.biz/techtips/pi-temperature_monitor

# easy install & run
sudo apt-get install git -y && git clone https://github.com/LukeKeam/pi-temperature_monitor && cd pi-temperature_monitor && python3 temperature_monitor.py

Tested on Raspberry Pi 4
Line 9 of temperature_monitor.py may change location of temperature in future 
temperature = os.popen("vcgencmd measure_temp").readline()