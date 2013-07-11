/**
 * softPwm test 
 * author:gootoomoon 
 * gcc -o test digital.c -lwiringPi -lpthread
 */
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <wiringPi.h>
#define OUTPUT 	1
#define HIGH 	1
#define LOW 	0

int pin = 1;

int main()
{
	if(wiringPiSetupPhys() == -1)
	{
		fprintf(stdout, "wiring lib init error:%s", strerror(errno));	
		return 1;
	}
	pinMode(pin,OUTPUT);

	for(;;){
		digitalWrite(pin,HIGH);
		delay(1000);
		digitalWrite(pin,LOW);
		delay(1000);
	}
}
