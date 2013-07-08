import wiringpi2
import sys

#this example need change script.bin
#[uart_para6]
#uart_used = 1
#uart_port = 6
#uart_type = 2
#uart_tx = port:PI12<3><1><default><default>
#uart_rx = port:PI13<3><1><default><default>
#PI12:  pin46[U14 Next to sata]
#PI13:  pin48[U14 Next to sata]
serial = wiringpi2.serialOpen('/dev/ttyS6',115200)
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

#####get data from serial

while 1:
	if wiringpi2.serialDataAvail(serial):
		val = wiringpi2.serialGetchar(serial)
		print chr(val)
#wiringpi2.serialClose(serial) # Pass in ID
