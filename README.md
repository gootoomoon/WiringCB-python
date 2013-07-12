**WiringCB for Python and c**
======================================

WiringPi: An implementation of most of the Arduino Wiring
	functions for the Raspberry Pi<br />
WiringPi2: WiringPi version 2 implements new functions for managing IO expanders.<br/>
WiringCB: Wiring like lib for cubieboard,change from  WiringPi2-Python<br/>

**sting:**

Build with gcc version 4.6.3 (ubuntu/linaro 12.10)
Built against Python 2.7.2, Python 3.2.3

**Prerequisites:**


You must have python-dev and python-setuptools installed <br/>
If you manually rebuild the bindings with swig -python wiringpi.i

**Get/setup repo:**


git clone https://github.com/gootoomoon/WiringCB-python.git

Python Start
-----------------------------

**Build & install with:**


	cd WiringCB-python
	sudo python setup.py install   # python 2.7.x
	sudo python3 setup.py install  # python 3.2.x

**Python Usage:**

	import wiringpi2
	OUTPUT = 1
	pin = 2
	HIGH = 1 
	LOW = 0	
		
	wiringpi2.wiringPiSetupPhys() # init pin to phy mode,U14(1~48) U15(49~96)
	wiringpi2.pinMode(pin,OUTPUT) # set pin 2 to output mode

	while 1:
		wiringpi2.digitalWrite(pin,HIGH) # Write HIGH to pin 2(U14 pin 2)
		wiringpi2.delay(1000)
		wiringpi2.digitalWrite(pin,LOW)  # Write LOW to pin
		wiringpi2.delay(1000)
		
**General IO:**

	wiringpi2.pinMode(2,1)      # Set pin 2 to output
	wiringpi2.digitalWrite(2,1) # Write 1 HIGH to pin 2
	wiringpi2.digitalRead(50)    # Read pin 50(U15 pin 2)

**Soft Tone**

Hook a speaker up to your Pi and generate music with softTone. Also useful for generating frequencies for other uses such as modulating A/C.

	wiringpi2.softToneCreate(PIN)
	wiringpi2.softToneWrite(PIN,FREQUENCY)

**Bit shifting:**

	wiringpi2.shiftOut(1,2,0,123) # Shift out 123 (b1110110, byte 0-255) to data pin 1, clock pin 2

**Serial:**

	serial = wiringpi2.serialOpen('/dev/ttyAMA0',9600) # Requires device/baud and returns an ID
	wiringpi2.serialPuts(serial,"hello")
	wiringpi2.serialClose(serial) # Pass in ID

**Full details at:**

http://www.wiringpi.com




C Start
------------------------------

**Build & install with:**

	cd WiringPi2-Python/WiringPi/
	./build.sh
	
**C Usage:**

	#include <wiringPi.h>
	
	#define OUTPUT 	1
	#define HIGH 	1
	#define LOW	0
	
	int pin = 1;
	
	int main()
	{
		wiringPiSetupPhys();  //init wiringCB lib
		pinMode(pin,OUTPUT);  //set pin to output mode
		for(;;){
			digitalWrite(pin,HIGH); //Write HIGH(1) to pin 
			delay(1000);		//delay for 1s
			digitalWrite(pin,LOW);	//Write LOW(0) to pin
			delay(1000);		//delay for 1s
		}
	}


compile code like this: gcc -o test test.c -lwiringPi -lpthread


