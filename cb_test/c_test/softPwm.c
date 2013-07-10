/**
 * softPwm test 
 * author:gootoomoon 
 * gcc -o test c_test_softPwm.c -lwiringPi -lpthread
 */
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <wiringPi.h>
#include <softPwm.h>

int pin = 1;

int main()
{
	int i;
	if(wiringPiSetupPhys() == -1)
	{
		fprintf(stdout, "wiring lib init error:%s", strerror(errno));	
		return 1;
	}
	softPwmCreate(pin,0,100);//set pin and range(0~100)

	for(;;){
	#if 1	
		//breathing LED
		for(i = 0;i < 100; i++)
		{
			softPwmWrite(pin, i);
			delay(10);
		}

		for(i = 100; i > 0; i--)
		{
			softPwmWrite(pin, i);	
			delay(10);
		}
	#endif
	#if 0
		softPwmWrite(pin,0);
		delay(1000);
		softPwmWrite(pin,50);
		delay(1000);
		softPwmWrite(pin,100);
		delay(1000);
	#endif
	}
}
