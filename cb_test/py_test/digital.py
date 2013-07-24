import wiringpi2
import sys

OUTPUT = 1
CHECK = 6
pin =1

wiringpi2.pinMode(pin,OUTPUT)
Mo = wiringpi2.pinMode(pin,CHECK)
MS = 1000

print "**********************"
print "delay:%s ms,Mode:%s" %(MS,Mo)
print "**********************"

while 1:
	wiringpi2.digitalWrite(pin,1)
	wiringpi2.delay(MS)
	wiringpi2.digitalWrite(pin,0)
	wiringpi2.delay(MS)
