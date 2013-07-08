import wiringpi2
import sys
pin = 31

#wiringpi2.wiringPiSetup()
#wiringpi2.wiringPiSetupSys()
#wiringpi2.wiringPiSetupGpio()
wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(pin,2)  #PWM_OUTPUT

wiringpi2.pwmSetClock(0); #24M/120=200k 
#range = 255
#HZ = 200k/(255+1) = 781hz
print "-------------"
wiringpi2.pwmWrite(pin,255);
print "-------------"

