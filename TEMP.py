import serial
import time
import os
os.system('clear')

print "HOME AUTOMATION & SECURITY SYSTEM "

while True:
    time.sleep(3)
    ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
    s=ser.read(32)
    print "THE Temperature iS(in DEGREE CELSIUS)"
    line=ser.readline()
    print line
    ser.close()

