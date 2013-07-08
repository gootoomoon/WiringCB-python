import wiringpi2

OUTPUT = 1
PIN_TO_PWM = 1  #pin 1 to output pwm

#wiringpi2.wiringPiSetup()
wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi2.softPwmCreate(PIN_TO_PWM,0,100)

for time in range(0,10): #time last 10s
	for brightness in range(0,100): 
		wiringpi2.softPwmWrite(PIN_TO_PWM,brightness)#M:S
		wiringpi2.delay(10) # Delay for 0.2 seconds
	for brightness in reversed(range(0,100)):
		wiringpi2.softPwmWrite(PIN_TO_PWM,brightness)
		wiringpi2.delay(10)

