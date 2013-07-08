import wiringpi2
import sys

serial = wiringpi2.serialOpen('/dev/ttyS5',115200)
wiringpi2.serialPuts(serial,"\n")
print serial
wiringpi2.serialPuts(serial,"Putchar:")
wiringpi2.serialPutchar(serial,0x38)#sent ascii 0x38: 8
#wiringpi2.serialPutchar(serial,0x65)#sent ascii 0x68: A
wiringpi2.serialPuts(serial,"\n")


wiringpi2.serialPuts(serial,"Puts:")
wiringpi2.serialPuts(serial,"hello\n")

wiringpi2.serialPuts(serial,"Printf:")
wiringpi2.serialPrintf(serial,"hello\n")
#wiringpi2.serialClose(serial) # Pass in ID

#serialFlush(serial)

#####get data from serial

while 1:
	if wiringpi2.serialDataAvail(serial):
		val = wiringpi2.serialGetchar(serial)
		print chr(val)
#wiringpi2.serialClose(serial) # Pass in ID
