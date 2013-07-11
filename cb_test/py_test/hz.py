#this func used to measure the frequency of GPIO of cubieboard
import wiringpi2
import sys

OUTPUT = 1
pin =1

#wiringpi2.wiringPiSetup()
wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(pin,OUTPUT)


while 1:
	wiringpi2.digitalWrite(pin,1)
	wiringpi2.digitalWrite(pin,0)
