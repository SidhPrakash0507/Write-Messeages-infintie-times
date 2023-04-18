import pyautogui as spam
import time 
limit=input(int("Enter no of messeges"))
msg=input(str("Enter the text you want to write"))
x=0
time.sleep(10)
while x<int(limit):
    spam.typewrite(msg)
    spam.press("enter")
x=x+1


    
    