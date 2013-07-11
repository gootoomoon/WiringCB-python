import wiringpi2
import sys

PUD_UP = 1
PUD_DOWN = 2
PUD_OFF = 0
pin =1
INPUT = 0

#wiringpi2.wiringPiSetup()
wiringpi2.wiringPiSetupPhys()
#wiringpi2.pinMode(pin,OUTPUT)
wiringpi2.pinMode(pin,INPUT)

while 1:
	wiringpi2.pullUpDnControl (pin, PUD_UP);
	val = wiringpi2.digitalRead(pin)
	print 'xxxxx UP'
	print val
	wiringpi2.delay(1000)
	wiringpi2.pullUpDnControl (pin, PUD_DOWN);
	val = wiringpi2.digitalRead(pin)
	print 'xxxxx DOWN'
	print val
	wiringpi2.delay(1000)
	wiringpi2.pullUpDnControl (pin, PUD_UP);
	val = wiringpi2.digitalRead(pin)
	print 'xxxxx UP'
	print val
	wiringpi2.delay(1000)
	wiringpi2.pullUpDnControl (pin, PUD_OFF);
	val = wiringpi2.digitalRead(pin)
	print 'xxxxx OFF'
	print val
	wiringpi2.delay(1000)
