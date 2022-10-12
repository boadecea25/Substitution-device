import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(26, GPIO.LOW)


#a = input("Enter value")
#b = input("Enter value")
#c = input("Enter value")
#d = input("Enter value")
#e = input("Enter value")
#f = input("Enter value")
#g = input("Enter value")
#h = input("Enter value")
#i = input("Enter value")
string = input("Enter string")
#string = a + b + c + d + e + f + g + h + i
dic = {1 : 26 , 2 : 23 , 3 : 17 , 4 : 24 , 5 : 27 , 6 : 13 , 7 : 22 , 8 : 25 , 9 : 19}



for x in range(9):
    k = string[x]
    if k == "1":
        GPIO.output(dic.get(x + 1), GPIO.HIGH)
        
    
    #if x == "1":
        #GPIO.output(dic.get(string.index(x) + 1), GPIO.HIGH)
        

time.sleep(2000)

GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(26, GPIO.LOW)

        

        
     




       


    
                
    
    
    
    
    
        
    
        

        
      
    



        
        
        







#GPIO.setup(17, GPIO.IN)
lpins=[]

#for i in range(500):
    #GPIO.output(17, GPIO.HIGH)
    #GPIO.output(27, GPIO.HIGH)
    #GPIO.output(22, GPIO.HIGH)
    #time.sleep(0.5)
    #GPIO.output(17, GPIO.LOW)
    #GPIO.output(27, GPIO.LOW)
    #GPIO.output(22, GPIO.LOW)
    #time.sleep(0.5)

# Infinite loop
#while True:
#    if GPIO.input(24) == 0:
#        # Turn off
#        GPIO.output(23, GPIO.LOW)
#    else:
#        # Turn on
#        GPIO.output(23, GPIO.HIGH)