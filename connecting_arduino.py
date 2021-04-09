#!/usr/bin/env python3
import serial
import time
from picamera import PiCamera
import os

import random

if __name__ == '__main__':
    
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout =1)
    ser.flush()
    camera = PiCamera()
    camera.rotation = 180
    
    
    while True:
        number = ser.read()
        if number != b'':
            if int.from_bytes(number, byteorder='big')==18:
                
                time.sleep(5)
                camera.capture('image1.jpg')
                
                motor_number = random.randint(1,3)
                print("Button has been pressed.")
                print("Sending number "+ str(motor_number)+ "to Arduino.")
                ser.write(str(motor_number).encode('utf-8'))
                time.sleep(5)

