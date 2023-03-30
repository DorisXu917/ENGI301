#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO  # import GPIO
from sensor_driver import HX711  # import the class HX711
#GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
hx = HX711(dout_pin="P2_4", pd_sck_pin="P2_2")  # create an object
print(hx.get_raw_data_mean())  # get raw data reading from hx711
GPIO.cleanup()