import RPi.GPIO as GPIO
import time
class moter:    
    def spin(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        servol=GPIO.PWM(11,50)
        servol.start(7.5)
        time.sleep(2)
        servol.ChangeDutyCycle(12.5)
        print("wait for 2 sec")
        time.sleep(2)
        servol.ChangeDutyCycle(7.5)
        servol.stop()
       
while True:
    GPIO.setmode(GPIO.BOARD)
    t=18
    e=16
    GPIO.setup(t,GPIO.OUT)
    GPIO.setup(e,GPIO.IN)
    m=moter()
    GPIO.output(t,True)
    time.sleep(0.00001)
    GPIO.output(t,False)
    while GPIO.input(e)==0:
        pulse_start =time.time()
    while GPIO.input(e)==1:
        pulse_end=time.time()
    ti=pulse_end-pulse_start
    distance=(ti*34000)/2
    dist=round(distance,2)
    if dist<=16:
        m.spin()

    print("Distance",dist)
   
    GPIO.cleanup()
    time.sleep(1)

