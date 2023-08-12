import RPi.GPIO as GPIO
from time import sleep
pir_gpio=27
led = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pir_gpio,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
while True :
    if GPIO.input(pir_gpio) == 1 :
        GPIO.output(led,GPIO.HIGH)
        print("Light is on")
        sleep(1) 
    else :
        GPIO.output(led,GPIO.LOW)
        print("Light is off")
        sleep(1)