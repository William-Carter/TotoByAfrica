import time

import sys
import os

try:
    import pygame


except:
    os.system("pip3 install pygame")

hoursbefore = 0
minutesbefore = 1
secondsbefore = 17



def getTime():
    uin = input("What time do you want the program to start the chorus at? Format in 24 hour time (00:00:00)\n")
    ulist = uin.split(":")
    hours = int(ulist[0])
    minutes = int(ulist[1])
    seconds = int(ulist[2])

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

pygame.init()
time.strftime("%H:%M:%S")
currenttime = str(time.strftime("%H:%M:%S"))
print("Program Start Time", currenttime)


timetogo = getTime()
#timetogo = "19:04:43"

print("\nProtocol will start at ", timetogo)
def play():
    print("\nProtocol Initiated")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    s = pygame.mixer.Sound(dir_path+"/africa.wav")
    s.play()
    
    while True:
        uin = input(">>")
        if uin == "quit":
            pygame.display.quit
            pygame.quit()
            os.system("killall Python")
            sys.exit(1)
        else:
            print("Type quit to kill program")
while True:
    currenttime = str(time.strftime("%H:%M:%S"))
    if currenttime == timetogo:
        play()
