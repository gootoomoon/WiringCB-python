#include <stdio.h>
#include <stdint.h>
#include "sunxi_cb_gpio.h"

/*
 *******************************
 * tool func for cubieboard
 * 
 */

/*
 *******************************
 * core func for cubieboard
 * 
 */

int sunxi_set_gpio_mode(int pin, int mode)
{
	uint32_t reg;

	printf ("I am sunxi set pin:%d to mode:%d\n", pin, mode) ;
	//reg = readl();
	if(0 ==  mode){ //INPUT
		
	} else if (1 == mode){ //OUTPUT
	
	}
	return 0;
}


