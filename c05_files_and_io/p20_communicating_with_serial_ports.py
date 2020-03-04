#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/3 20:03
# @File    : p20_communicating_with_serial_ports.py
# @Software: PyCharm

"""与串行端口的数据通信"""

import serial

# 使用pySerial包
ser = serial.Serial('/dev/tty.usbmodem641', baudrate=9600, bytesize=8, parity='N', stopbits=1)
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
