import webbrowser
import pyautogui, webbrowser
import time

webbrowser.open("https://web.whatsapp.com/send?phone=+") #Number with lada after "+"
time.sleep(20)  #Time for the browser to init and open Whatsapp Web
i=0
while(i<100):   #Number of times that the message will be sended
    pyautogui.typewrite("") #Message
    pyautogui.press("enter")
    i+=1
    time.sleep(0.3)
