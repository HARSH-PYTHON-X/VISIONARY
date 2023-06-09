from time import sleep
import speech_recognition as sr
import pyttsx3
import pyautogui
import pydirectinput
import webbrowser
import datetime

print()
print('----------------------------------------')
print('DYNAMIX CORPORATION - CYBERDEX /TERMINATOR TR-X')
print('----------------------------------------')
print()

def speak (what_to_say) :
    engine = pyttsx3.init()
    engine.say(what_to_say)
    engine.runAndWait()

def wishme () :
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12 :

        print('GOOD MORNING SIR')

        speak('good morning sir')

    elif hour >=12 and hour <= 18 :

        print('GOOD AFTERNOON SIR')

        speak('good afternoon sir')

    else :

        print('GOOD EVENING SIR')

        speak('good evening sir')

    print('I am / TERMINATOR TR-X')
    speak('I am TERMINATOR TRX')

    print()

    print('WHAT CAN I DO FOR YOU')
    speak('what can i do for you')

    print()

def take_command () :
    r = sr.Recognizer()

    with sr.Microphone() as source :
        print('listening ...')
        audio = r.listen(source)

        try :
            cmd = r.recognize_google(audio)
            print('command >',cmd)

        except Exception as e :
            print('please command again')
            speak('please command again')

            return 'None'
        return cmd

if __name__ == '__main__':
    wishme()

    while True :
        cmd = take_command().lower()

        # WORD DONE MENTIONER

        def work_done () :
            print('work done sir')
            speak('work done sir')

        # INTRODUCTION OF TERMINATOR 

        def introduce_terminator () :
            print('I am TERMINATOR succesor TERMINATOR - TR X, I am designed from inspiration by JARVIS and TERMINATOR from IRON MAN series. My main work is to control data bases and help my Creater, aka [HARSH] in 3d designing and programming. Thank you.')
            speak('I am TERMINATOR succesor TERMINATOR - TR X, I am designed from inspiration by JARVIS and TERMINATOR from IRON MAN series. My main work is to control data bases and help my Creater, aka [HARSH] in 3d designing and programming. Thank you.')
            work_done

        # OPEN CHROME

        def open_chrome () :
            print('opening chrome sir...')
            speak('opening chrome sir')
            webbrowser.open('C:\\Users\\Owner\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe')
            work_done()

        # OPEN YOUTUBE

        def open_youtube () :
            print('opening youtube sir...')
            speak('opening youtube sir')
            webbrowser.open('https://youtube.com/')
            work_done()

        # OPEN VSCODE

        def open_code () :
            print('opening VSCODE sir...')
            speak('opening vscode sir')
            webbrowser.open('"C:\\Users\\Owner\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
            work_done()

        # OPEN PAINT

        def open_paint () :
            print('opening paint sir...')
            speak('opening paint sir')
            webbrowser.open('mspaint')
            work_done()

        # OPEN NOTEPAD

        def open_notepad () :
            print('opening notepad sir...')
            speak('opening notepad sir')
            webbrowser.open('notepad')
            work_done()

        # OPEN NASA WEBSITE

        def open_nasa () :
            print('opening NASA website sir...')
            speak('opening NASA webdite sir')
            webbrowser.open('www.nasa.gov.in')
            work_done()

        # OPEN COMMAND PROMPT

        def open_cmd () :
            print('opening command prompt sir...')
            speak('opening command prompt sir')
            webbrowser.open('cmd')
            work_done()

        # DESTROY CODE

        def destroy_code () :
            speak('initialising destroy code sequence in 5 seconds')

            print('initialising destroy code sequence in 5 seconds')

            sleep(5)

            pyautogui.hotkey('Ctrl' , 'a')
            pyautogui.press('Backspace')

            speak('Sucessfully destroyed code')

            print('Sucessfully destroyed Code')

        # RECOVER CODE 

        def recover_code () :
            speak('recovering code in 5 seconds')

            print('recovering code in 5 seconds')

            sleep(5)

            pyautogui.hotkey('Ctrl' , 'z')

            speak('sucessfully code recovered')

            print('sucessfully code recovered')


        # GENERATE CALCULATOR

        def generate_calculator () :
            speak('generating code to create CALCULATOR in 5 seconds')
            
            print()
            print('starting code for CALCULATOR in 5 seconds  !!!')
            print()
            
            def wait() :
                
                sleep(0.5)
                
            def type(what_to_type) :
                
                pyautogui.write(what_to_type)
                
            def enter() :
                pyautogui.press('Enter')
                pyautogui.press('Enter')
                
            sleep(5)
            
            pyautogui.write("num1 = int(input('NUM 1 >>'))")
            
            sleep(0.5)
            
            pyautogui.press('Enter')
            
            sleep(0.5)
            
            pyautogui.write("func = int(input('Function >>'))")
            
            sleep(0.5)
            
            pyautogui.press('Enter')
            
            pyautogui.write("num2 = int(input('NUM 2 >>'))")
            
            wait()
            enter()
            
            type("add = num1 + num2")
            
            wait()
            enter()
            
            type("sub = num1 - num2")
            
            wait()
            enter()
            
            type("div = num1 / num2")
            
            wait()
            enter()
            
            type("multiply = num1 * num2")
            
            wait()
            enter()
            
            pyautogui.press('Enter')
            
            type("if func == ('+') :")
            
            wait()
            enter()
            
            type("print(add)")
            
            wait()
            enter()
            
            pyautogui.press('Backspace')
            
            type("if func == ('-') :")
            
            wait()
            enter()
            
            type('print(sub)')
            
            wait()
            enter()
            
            pyautogui.press('Backspace')
            
            type("if func == ('*') :")
            
            wait()
            enter()
            
            type('print(multiply)')
            
            wait()
            enter()
            
            pyautogui.press('Backspace')
            type("if func == ('/') :")
            
            wait()
            enter()
            
            type('print(div)')

            work_done()



        # GENERATE AI

        def generate_AI () :
            def wait() :
    
                sleep(0.5)

            def type(what_to_type_ai) :

                pyautogui.write(what_to_type_ai) 

            speak('generating code to create AI in 5 seconds')

            print()
            print('generating code to CREATE AI in 5 seconds')
            print()

            sleep(5)

            type("import pyttsx3")
            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type('import speech_recognition as sr')

            wait()
            pyautogui.press('Enter')
            wait()

            type('import subprocess')

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type('import webbrowser')

            wait()
            pyautogui.press('Enter')
            wait()

            pyautogui.press('Enter')
            wait()

            pyautogui.press('Enter')
            wait()

            type('engine = pyttsx3.init()')
            
            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type("def speak(what_to_speak) :")
            wait()
            pyautogui.press('Enter')
            wait()

            type("engine.say(what_to_speak)")
            wait()
            pyautogui.press('Enter')
            wait()

            type("engine.runAndWait()")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            pyautogui.press('Backspace')

            wait()

            type("def wishme() :")

            wait()
            pyautogui.press('Enter')
            wait()

            type("speak('welcome sir')")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Backspace')
            wait()

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

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type("if 'open notepad' in cmd :")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type("speak('opening notepad')")
            
            wait()
            pyautogui.press('Enter')
            wait()
            
            type("subprocess.call('notepad')")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Backspace')
            wait()

            type("elif 'open command' in cmd :")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type("speak('opening command prompt')")

            wait()
            pyautogui.press('Enter')
            wait()

            type("webbrowser.open('cmd.exe')")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Backspace')
            wait()

            type("elif 'terminate' in cmd :")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type("speak('terminating AI')")

            wait()
            pyautogui.press('Enter')
            wait()
            pyautogui.press('Enter')
            wait()

            type("break")

            speak('Sucessfully Code written')

            print('Sucessfully Code written')

            print()


        # MATRIX

        def matrix () :
            speak('Iniatialising Hack squence in command prompt sir...')

            print('initialising Hack squence in command promp sir')

            webbrowser.open('cmd.exe')

            sleep(1.5)

            pyautogui.write('color a')

            sleep(0.5)

            pyautogui.press('Enter')

            sleep(0.5)

            pyautogui.write('dir/s')

            sleep(0.5)

            pyautogui.press('Enter')

            work_done()

        # OPEN FUSION 360

        def open_fusion_360 () :
            speak('opening FUSION 360 sir')
            print('opening FUSION 360 sir ...')
            webbrowser.open('C:\\users\\Owner\\AppData\\Local\\Autodesk\\webdeploy\\production\\6a0c9611291d45bb9226980209917c3d\\FusionLauncher.exe')

        # OPEN ONSHAPE

        def open_onshape () :
            speak('opening ONSHAPE sir')
            print('opening ONSHAPE sir ...')
            webbrowser.open('C:\\Users\\Owner\\AppData\\Local\\Google\\Chrome\\Application\\chrome_proxy.exe  --profile-directory=Default --app-id=okfmenfcdfongamkkglabpooahidmmad')

        # TERMINATE 

        def terminate () :
            print('terminating myself sir')
            speak('terminating myself sir')

        # NEURAL NETWORK

        # INTRODUCE TERMINATOR

        if 'who are you' in cmd :
            introduce_terminator()

        elif 'terminator who are you' in cmd :
            introduce_terminator()

        elif 'terminator introduce yourself' in cmd :
            introduce_terminator()

        elif 'who you are' in cmd :
            introduce_terminator()

        elif 'why you are' in cmd :
            introduce_terminator()

        elif 'who is terminator' in cmd :
            introduce_terminator()

        elif 'why is terminator' in cmd :
            introduce_terminator()

        elif 'who are you terminator' in cmd :
            introduce_terminator()

        # OPEN CHROME

        elif 'open chrome' in cmd :
            open_chrome()

        elif 'terminator open chrome' in cmd :
            open_chrome()

        elif 'open chrome terminator' in cmd :
            open_chrome()

        # OPEN YOUTUBE

        elif 'open youtube' in cmd :
            open_youtube()

        elif 'terminator open youtube' in cmd :
            open_youtube()

        elif 'open youtube terminator' in cmd :
            open_youtube()

        # OPEN VSCODE

        elif 'open code' in cmd :
            open_code()

        elif 'open code terminator' in cmd :
            open_code()

        elif 'terminator open code' in cmd :
            open_code()

        # OPEN PAINT

        elif 'open paint' in cmd :
            open_paint()

        elif 'open paint terminator' in cmd :
            open_paint()

        elif 'terminator open paint' in cmd :
            open_paint()

        # OPEN NOTEPAD

        elif 'open notepad' in cmd :
            open_paint()

        elif 'open notepad terminator' in cmd :
            open_paint()

        elif 'terminator open notepad' in cmd :
            open_paint()

        # OPEN NASA WEBSITE

        elif 'open nasa' in cmd :
            open_nasa()

        elif 'open nasa terminator' in cmd :
            open_nasa()

        elif 'terminator open nasa' in cmd :
            open_nasa()

        elif 'open nasa website' in cmd :
            open_nasa()

        # OPEN COMMAND PROMPT

        elif 'open cmd' in cmd :
            open_cmd()

        elif 'open command prompt' in cmd :
            open_cmd()

        elif 'open cmd terminator' in cmd :
            open_cmd()

        elif 'open command prompt terminator' in cmd :
            open_cmd()

        elif 'terminator open cmd' in cmd :
            open_cmd()

        elif 'terminator open command prompt' in cmd :
            open_cmd()


        # GENERATE CALCULATOR

        elif 'generate calculator' in cmd :
            generate_calculator()

        elif 'generate calculator terminator' in cmd :
            generate_calculator()

        elif 'terminator generate calculator' in cmd :
            generate_calculator()

        elif 'create calculator' in cmd :
            generate_calculator()

        elif 'create calculator terminator' in cmd :
            generate_calculator()

        elif 'terminator create calculator' in cmd :
            generate_calculator()

        
        # GENERATE AI

        elif 'generate ai' in cmd :
            generate_AI()

        elif 'generate ai terminator' in cmd :
            generate_AI()

        elif 'terminator generate ai' in cmd :
            generate_AI()

        elif 'create ai' in cmd :
            generate_AI()

        elif 'create ai terminator' in cmd :
            generate_AI()

        elif 'terminator create ai' in cmd :
            generate_AI()

        elif 'generate artificial intelligence' in cmd :
            generate_AI()

        elif 'generate artificial intelligence terminator' in cmd :
            generate_AI()

        elif 'terminator generate artificial intelligence' in cmd :
            generate_AI()


        # MATRIX

        elif 'initialize matrix system' in cmd :
            matrix()

        elif 'initialize matrix' in cmd :
            matrix()

        elif 'terminator matrix' in cmd :
            matrix()

        elif 'matrix' in cmd :
            matrix()

        elif 'matrix terminator' in cmd :
            matrix()

        # DESTROY CODE

        elif 'destroy code' in cmd :
            destroy_code()

        elif 'delete code' in cmd :
            destroy_code()

        elif 'destroy code terminator' in cmd :
            destroy_code()

        elif 'delete code terminator' in cmd :
            destroy_code()

        elif 'terminator destroy code' in cmd :
            destroy_code()

        elif 'terminator delete code' in cmd :
            destroy_code()

        # RECOVER CODE

        elif 'recover code' in cmd :
            recover_code()

        elif 'recover code terminator' in cmd :
            recover_code()

        elif 'terminator recover code' in cmd :
            recover_code()

        # OPEN FUSION 360

        elif 'open fusion 360' in cmd :
            open_fusion_360()

        elif 'terminator open fusion 360' in cmd :
            open_fusion_360()

        elif 'open fusion 360 terminator' in cmd :
            open_fusion_360()

        # OPEN ONSHAPE

        elif 'open onshape' in cmd :
            open_onshape()

        elif 'terminator open onshape' in cmd :
            open_onshape()

        elif 'open onshape terminator' in cmd :
            open_onshape()
 
        # TERMINATE

        elif 'terminate' in cmd :
            terminate()
            break

        elif 'terminate terminator' in cmd :
            terminate()
            break

        elif 'terminate yourself' in cmd :
            terminate()
            break
