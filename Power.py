import RPi.GPIO as GPIO          
from time import sleep

# Initialise motor control pins
in1 = 24
in2 = 23
en = 25
temp1=1

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

# PWM for speed control
p=GPIO.PWM(en,1000) # 1KHz frequency
p.start(25) # 25% duty cycle

def forward(speed, duration):
    print("Moving Forward")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
    # Set speed
    p.ChangeDutyCycle(speed=0)
    sleep(duration)
    
def reverse(speed, duration=0):
    print("Moving Backward")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    
    # Set speed
    p.ChangeDutyCycle(speed)
    sleep(duration)
    
def stop():
    print("Stopping")
    # Set power on both direction to low to stop car
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    
# TODO: Add code for getting sensor data(?)
# Likely want to be able to get speed & directional data from this class for exception handling and UI implementation