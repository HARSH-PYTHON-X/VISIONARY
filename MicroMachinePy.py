from time import sleep
import random
import pyautogui
import pydirectinput as pd
import cv2 
import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess

#! SPEAK

def speak (txt) :
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

#! RANDOM 

def return_random (element = None, length = 1) :
    random_ans = ''.join(random.sample(element, length))

    return random_ans

#! SPEECH_RECOGNITION 

def create_listening_pool (delay = 7) :
    def type (txt) :
        pyautogui.write(txt)

    def wait (delay = 0.5) :
        sleep(delay)

        type("def take_command() :")
            
        wait()
        pyautogui.press('Enter')
        wait()
            
        type("r = sr.Recognizer()")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type("with sr.Microphone() as source :")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type("print('listening ...')")

        wait()
        pyautogui.press('Enter')
        wait()

        type("audio = r.listen(source)")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type('try :')

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type("cmd = r.recognize_google(audio)")

        wait()
        pyautogui.press('Enter')
        wait()

        type("print('you said : {}'.format(cmd))")                      # THIS CAN CREATE PROBLEM

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()
            
        pyautogui.press('Backspace')
        wait()

        type("except Exception as e :")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type("speak('please speak again')")
            
        wait()
        pyautogui.press('Enter')
        wait()

        type("print('please speak again')")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type("return 'None'")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Backspace')
        wait()

        type("return cmd")

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Backspace')
        wait()

        type("if __name__ == '__main__' :")
            
        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type('wishme()')

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type('while True :')

        wait()
        pyautogui.press('Enter')
        wait()
        pyautogui.press('Enter')
        wait()

        type("cmd = take_command().lower()")
