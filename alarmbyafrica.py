import time
import pygame
import sys
import os

hoursbefore = 0
minutesbefore = 1
secondsbefore = 17
seconds = 0
minutes = 0
hours = 0
hourslater = 0
minuteslater = 0
secondslater = 0
pygame.init()

def newTime():
    global hours, minutes, seconds, hourslater, secondslater, minuteslater, timetogo
    seconds += secondslater
    if seconds >= 60:
        minutes += 1
        seconds -= 60

    minutes += minuteslater
    if minutes >= 60:
        hours += 1
        minutes -= 60

    hours += hourslater
    if hours >= 24:
        hours -= 24

    return str(hours)+":"+str(minutes)+":"+str(seconds)

def getTime():
    global hours, minutes, seconds
    global hourslater, minuteslater, secondslater
    
    uin = input("What time do you want the program to start the chorus at? Format in 24 hour time (00:00:00)\n")
    ulist = uin.split(":")
    hours = int(ulist[0])
    minutes = int(ulist[1])
    seconds = int(ulist[2])

    interval = input("And at what interval?\n")



    ilist = interval.split(":")
    hourslater = int(ilist[0])
    minuteslater = int(ilist [1])
    secondslater = int(ilist[2])
    

    seconds -= secondsbefore
    if seconds < 0:
        minutes -= 1
        seconds += 60

    

    
    minutes -= minutesbefore
    if minutes < 0:
        hours -= 1
        minutes += 60

    


    hours -= hoursbefore
    if hours < 0:
        hours += 24


    if len(str(seconds)) < 2:
        seconds = "0"+str(seconds)

    if len(str(minutes)) < 2:
        minutes = "0"+str(minutes)

    if len(str(hours)) < 2:
        hours = "0"+str(hours)



    return (str(hours)+":"+str(minutes)+":"+str(seconds))



def play():
    print("\nProtocol Initiated")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    s = pygame.mixer.Sound(dir_path+"/africa.wav")
    s.play()
    
    global timetogo
    timetogo = newTime()
    


timetogo = getTime()
print(timetogo)
while True:
    currenttime = str(time.strftime("%H:%M:%S"))
    if currenttime == timetogo:
        play()
