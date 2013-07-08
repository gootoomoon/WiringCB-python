import wiringpi2
import sys
pin = 31

wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(pin,2)  #PWM_OUTPUT

#wiringpi2.pwmSetClock(0); #24M/120=200k 
#range = 255
#HZ = 200k/(255+1) = 781hz

while 1:
	for brightness in range(0,255):
		wiringpi2.pwmWrite(pin,brightness);
		wiringpi2.delay(10)
		print brightness
	for brightness in range(0,255):
		wiringpi2.pwmWrite(pin,255-brightness)
		wiringpi2.delay(10)
		hello = 255 - brightness
		print hello

