#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# gps_time_ex2.py
#
# Simple Example for SparkFun ublox GPS products 
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, July 2020
# 
# Do you like this library? Help support SparkFun. Buy a board!
# https://sparkfun.com
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 2
# This example sets up the serial port and then passes it to the UbloxGPs
# library. From here we call date_time() and to get gps time and check whether
# the data received is "valid" which indicates that the probability of the time
# to be correct is very high. 

import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():

    try:
        print("Listening for UBX Messages")
        while True:
            try:
                gps_time = gps.date_time()
                print("{}/{}/{}".format(gps_time.day, gps_time.month,
                                          gps_time.year))
                print("UTC Time {}:{}:{}".format(gps_time.hour, gps_time.min,
                                          gps_time.sec))
                print("Valid date:{}\nValid Time:{}".format(gps_time.valid.validDate, 
                                                             gps_time.valid.validTime))
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()
