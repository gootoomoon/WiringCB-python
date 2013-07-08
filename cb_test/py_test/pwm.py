import wiringpi2
import sys
pin = 31

#wiringpi2.wiringPiSetup()
#wiringpi2.wiringPiSetupSys()
#wiringpi2.wiringPiSetupGpio()
wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(pin,2)  #PWM_OUTPUT

while 1:
	#wiringpi2.pwmWrite(pin,128)
	print "111111 set clock"
	wiringpi2.pwmSetClock(0) # 24M/120 
	wiringpi2.delay(1000)
	wiringpi2.pwmSetClock(1);
	wiringpi2.delay(1000)
	wiringpi2.pwmSetClock(2);
	wiringpi2.delay(1000)
	print "222222 pwmWrite"
	#wiringpi2.pwmSetRange(255);
	wiringpi2.pwmWrite(pin,1);
	wiringpi2.delay(1000)
	wiringpi2.pwmWrite(pin,128);
	wiringpi2.delay(1000)
	wiringpi2.pwmWrite(pin,255)
	wiringpi2.delay(1000)
	print "================>>>>"
#	pwmSetMode(0);
	#wiringpi2.pwmWrite(pin,128)
