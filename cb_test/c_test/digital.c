/**
 * softPwm test 
 * author:gootoomoon 
 * gcc -o test c_digital.c -lwiringPi -lpthread
 */
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <wiringPi.h>

int pin = 1;

int main()
{
	if(wiringPiSetupPhys() == -1)
	{
		fprintf(stdout, "wiring lib init error:%s", strerror(errno));	
		return 1;
	}

	for(;;){
		digitalWrite(pin,1);
		delay(1000);
		digitalWrite(pin,0);
		delay(1000);
	}
}
