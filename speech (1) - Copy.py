# import required module
import speech_recognition as sr
import serial
import time
import RPi.GPIO as GPIO


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



def lights(c):
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    
    dic = {1 : 26 , 2 : 23 , 3 : 17 , 4 : 24 , 5 : 27 , 6 : 13 , 7 : 22 , 8 : 25 , 9 : 19}
    for x in range(9):
            k = c[x]
            if k == "1":
                    GPIO.output(dic.get(x + 1), GPIO.HIGH)
        
                
        
    
       
    

    time.sleep(5)

    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)

#ser=serial.Serial("COM5",2*10**6)
#def readport(x):
   #while 1:
        #y=ser.readline().decode().rstrip()
        #print(y)
        #if y==x:

                #break
#         time.sleep(0.001)     
#readport('a')
while 1:
        # explicit function to take input commands
        # and recognize them
      

        
        def takeCommandHindi():
                print(1)	
                r = sr.Recognizer()
                with sr.Microphone() as source:
		
                # seconds of non-speaking audio before
		# a phrase is considered complete
                        print('Listening')
                        r.pause_threshold = 1.0
                        audio = r.listen(source)
                        try:
                                print("Recognizing")
                                Query = r.recognize_google(audio, language='hi-In')
			
			# for listening the command in indian english
                                print( Query)
		
		# handling the exception, so that assistant can
		# ask for telling again the command
                        except Exception as e:
                                print(e)
                                print("Say that again sir")
                                return "None"
                        return Query



# Driver Code
		
# call the function

        import re
  
# initializing string
        test_str = takeCommandHindi()
# using sub() to perform substitutions
# ord() for conversion.
        res = (re.sub('.', lambda x: r'\u % 04X' % ord(x.group()), test_str))
        t=""  
# printing result 
        st=str(res).replace(r'\u '  , "")
        print(st)
        st=st+" "
        s=""
        m=[]
        n=[]
        h=0
        for i in range(len(st)):
                c=""
                if st[i]!=" " and i<len(st) :
                        s+=st[i]
                
                else:
                        print(s)
               
                        if s=="93E":
                                s="94D"+"906"
                        if s=="93F":
                                s="94D"+"907"
                        if s=="940":
                                s="94D"+"908"
                        if s=="941":
                                s="94D"+"909"
                        if s=="942":
                                s="94D"+"90A"
                        if s=="943":
                                s="94D"+"90B"
                        if s=="944":
                                s="94D"+"90C"
                        if s=="945":
                                s="94D"+"90D"
                        if s=="946":
                                s="94D"+"90E"
                        if s=="947":
                                s="94D"+"90F"
                        if s=="948":
                                s="94D"+"910"
                        if s=="949":
                                s="94D"+"911"
                        if s=="94A":
                                s="94D"+"912"
                        if s=="94B":
                                s="94D"+"913"
                        if s=="94C":
                                s="94D"+"914"
                        if s[0:3]!="94D":#[1 4 7;2 5 8;3 6 9]
                                if s=="901":
                                      c="001000000"
                                if s=="902":
                                      c="000011000"
                                if s=="903":
                                      c="000001000"
                                if s=="905":
                                      c="100000000"
                                if s=="906":
                                      c="001110000"
                                if s=="907":
                                      c="010100000"
                                if s=="908":
                                      c="001010000"
                                if s=="909":
                                      c="101001000"
                                if s=="90A":
                                      c="110011000"
                                if s=="90B":
                                      c="111010010"
                                if s=="90C":
                                      c="111000010"
                                if s=="90E":
                                      c="010001000"
                                if s=="910":
                                      c="001100000"
                                if s=="90F":
                                      c="100010000"
                                if s=="912":
                                      c="101101000"
                                if s=="913":
                                      c="101010000"
                                if s=="914":
                                      c="010101000"
                                if s=="915":
                                      c="101000000"
                                if s=="916":
                                      c="000101000"
                                if s=="917":
                                      c="110110000"
                                if s=="918":
                                      c="110001000"
                                if s=="919":
                                      c="001101000"
                                if s=="91A":
                                      c="100100000"
                                if s=="91B":
                                      c="100001000"
                                if s=="91C":
                                      c="010110000"
                                if s=="91D":
                                      c="001011000"
                                if s=="92F":
                                      c="010010000"
                                if s=="920":
                                      c="010111000"
                                if s=="921":
                                      c="110101000"
                                if s=="922":
                                      c="111111000"
                                if s=="923":
                                      c="001111000"
                                if s=="924":
                                      c="011110000"
                                if s=="925":
                                      c="100111000"
                                if s=="926":
                                      c="100110000"
                                if s=="927":
                                      c="011101000"
                                if s=="928":
                                      c="101110000"
                                if s=="92A":
                                      c="111100000"
                                if s=="92B":
                                      c="011010000"
                                if s=="92C":
                                      c="110000000"
                                if s=="92D":
                                      c="000110000"
                                if s=="92E":
                                      c="101100000"
                                if s=="92F":
                                      c="101111000"
                                if s=="930":
                                      c="111010000"
                                if s=="932":
                                      c="111000000"
                                if s=="933":
                                      c="000111000"
                                if s=="935":
                                      c="111001000"
                                if s=="936":
                                      c="100101000"
                                if s=="937":
                                      c="111101000"
                                if s=="938":
                                      c="011100000"
                                if s=="939":
                                      c="110010000"
                                if s=="95C":
                                      c="110111000"
                                if s=="95D":
                                      c="110111010"
                                if s=="95E":
                                      c="110100000"
                                if s=="95B":
                                      c="101011000"
                                if s=="93D":
                                      c="010000000"
                                if s=="967":#1
                                      c="100111010"
                                if s=="968":#2
                                      c="110111010"
                                if s=="969":#3
                                      c="111111010"
                                if s=="96A":#4
                                      c="111110010"
                                if s=="96B":#5
                                      c="111111100"
                                if s=="96C":#6
                                      c="111001010"
                                if s=="96D":#7
                                      c="100111000"
                                if s=="96E":#8
                                      c="000111110"
                                if s=="96F":#9
                                      c="111110110"
                                if s=="970":#0
                                      c="111110100"
                                if s=="020":
                                      c="000000000"
                        else:
                       
                                if s[3:]=="906":
                                      c="001110001"
                                if s[3:]=="907":
                                      c="010100001"
                                if s[3:]=="908":
                                      c="001010001"
                                if s[3:]=="909":
                                      c="101001001"
                                if s[3:]=="90A":
                                      c="110011001"
                                if s[3:]=="90B":
                                      c="111010011"
                                if s[3:]=="90C":
                                      c="111000011"
                                if s[3:]=="90E":
                                      c="010001001"
                                if s[3:]=="910":
                                      c="001100001"
                                if s[3:]=="90F":
                                      c="100010001"
                                if s[3:]=="912":
                                      c="101101001"
                                if s[3:]=="913":
                                      c="101010001"
                                if s[3:]=="914":
                                      c="010101001"
                        
                        if c=="":
                                c="000000000"
                        n.append(s)
                        m.append(c)
                        s=""
        
        for i in range(len(n)):
                if n[i][0:3]=="94D":
                        m[i-1]=m[i-1][0:8]+"1"
        print(m)
        i=1
        
        x=''
for c in m:
        lights(c)
return c




        #for i in range(len(m)):
                #ser.write(str(int(m[i],2)).encode())
                #readport('k')
        #ser.write("000000000".encode())       

#ser.close()
      


