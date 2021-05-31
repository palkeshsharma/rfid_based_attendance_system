"""
Created on Sun Apr  2 01:38:43 2020

@author: Shivani Kushwah 
"""

from serial import Serial
import signal

arduino = Serial('COM3', 9600) #, timeout=.1) # wait for Arduino
dat = arduino.readline().decode('ascii')
if(dat):
        print("Read\n")       
                

        
        
                


        



