import wiringpi2
import sys

OUTPUT = 1
pin =1

#wiringpi2.wiringPiSetup()
wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(pin,OUTPUT)

MS = 1000

print "*************"
print MS
print "*************"

while 1:
	wiringpi2.digitalWrite(pin,1)
	wiringpi2.delay(MS)
	wiringpi2.digitalWrite(pin,0)
	wiringpi2.delay(MS)
