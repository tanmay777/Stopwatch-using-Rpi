import RPi.GPIO as GPIO
import time

LED=18
BUTTON=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.output(LED,GPIO.LOW)

try:
	#preserve system resources with sleep() by preventing constant polling for input
	while True:
		if(GPIO.input(BUTTON)==0):
			print "Started Timer"
			start_time=time.time()
		if(GPIO.input(BUTTON)==1)
			print "Timer stopped"
			end_time=time.time()
			print "Time"+str(end_time-start_time)
	except KeyboardInterrupt:
		GPIO.cleanup()
