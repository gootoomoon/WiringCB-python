import wiringpi2
import sys
OUTPUT = 1
PIN_TO_PWM = 1  #pin 1 to output pwm

#wiringpi2.wiringPiSetup()
wiringpi2.wiringPiSetupPhys()
wiringpi2.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi2.softPwmCreate(PIN_TO_PWM,0,100)

time = wiringpi2.millis();
print "----------milliseconds-------------"
print   time
print "-----------------------------------"
time = wiringpi2.micros();
print "----------microseconds-------------"
print time
print "-----------------------------------"
