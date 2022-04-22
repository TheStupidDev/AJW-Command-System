#basic modules setup
import traceback
import sys
import os
import subprocess
import time
import random
import shutil
import psutil
import linecache
from pathlib import Path

#basic setup
wait = time.sleep
workingdir = os.getcwd()
conferrinfo='!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def loading():
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.08)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print()


#config
version = "v0.30" #note to myself: modify this later on next versions

errorinfo = 0
simplemode = 0

configpath = 'ajwconfig.txt'
path = Path(configpath)

def configreset():
    print("Error reading config! Rewriting config!")
    with open('ajwconfig.txt', 'w+') as f:
        f.write("errorinfo     = true\n")
        f.write("simplemode    = false\n")
        f.write("enablelogging = true\n")
        f.write("\n#================================================")
        f.write("\n#>Do not change position of the config or it will break (But you can change the value to true/false)")
        f.write("\n#>Logs can be found in 'ajwlog.txt' ")
        wait(0.1)
        checkline()
        print("Config re-written, please restart program")

try:
    if path.is_file():
        configfile = open("ajwconfig.txt")
        configlines = configfile.readlines()
        configlines = [line.replace(' ', '') for line in configlines]#remove all space in the file

        #list of configs
        errorinfo = configlines[0].lower()#errorinfo-line 1
        simplemode = configlines[1].lower()#simplemode-line 2
        enablelogging = configlines[2].lower()#enablelogging-line 3
    else:
        configreset()

except Exception:
    print(conferrinfo)   

#for modders
modded = 0 #0=Not Modded, 1=Modded
modname = "[Your Mod Name]"
modauthor = "[Your Name]"
modversion = "[Your Mod Version]"

def info():
    print("""
                  ___          _______                                          _  _____           _                 
        /\       | \ \        / / ____|                                        | |/ ____|         | |                
       /  \      | |\ \  /\  / / |     ___  _ __ ___  _ __ ___   __ _ _ __   __| | (___  _   _ ___| |_ ___ _ __ ___  
      / /\ \ _   | | \ \/  \/ /| |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |\___ \| | | / __| __/ _ \ '_ ` _ \ 
     / ____ \ |__| |  \  /\  / | |___| (_) | | | | | | | | | | | (_| | | | | (_| |____) | |_| \__ \ ||  __/ | | | | |
    /_/    \_\____/    \/  \/   \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|_____/ \__, |___/\__\___|_| |_| |_|
                                                                                          __/ |                      
                                                                                         |___/
    """)                                                                                     

    print(f"Welcome to the AJW Command System ({version} BETA)!")
    print("Type >help to find out all the commands")



def checkline():
    if simplemode == 'simplemode=false\n':
        print("==============================================")
    elif simplemode == 'simplemode=true\n':
        pass
    else:
        print("**********************************************")


def checkloading():
    if simplemode == 'simplemode=false\n':
        loading()
    elif simplemode == 'simplemode=true\n':
        pass
    else:
        print("??????????????????????????????????????????????")
                
#unlooped stuff
try:
    if simplemode == 'simplemode=false\n':
        info()
    elif simplemode == 'simplemode=true\n':
        print("AJW Command System")
    else:
        configreset()
        
except Exception:
    print(conferrinfo)

while True:
#looped stuff
    try:
    #basic program setup
        print("----------------------------------------------")

    #check simplemode
        try:
            if simplemode == 'simplemode=false\n':
                print(f"[{workingdir}]")
            elif simplemode == 'simplemode=true\n':
                pass
            else:
                print("[err]")
                
        except Exception:
            print(conferrinfo)
                
        cmd = (input(f"Enter a command: ")).lower()
        print("----------------------------------------------")

    #check enablelogging
        try:
            logpath = 'ajwlog.txt'
            zepath = Path(logpath)

            if zepath.is_file():

                import datetime
                today = datetime.date.today()
                zday = today.strftime("%d/%m/%Y")
                
                now = datetime.datetime.now()
                ztime = now.strftime("%H:%M:%S")

                if enablelogging == 'enablelogging=false\n':
                    pass
                
                elif enablelogging == 'enablelogging=true\n':
                    with open('ajwlog.txt', 'r') as log:
                        before = log.read()
                        log.close()

                    with open('ajwlog.txt', 'w+') as log:
                        log.write(f"{before}\n{zday} | {ztime} | Used the command {cmd}")
                        log.close()
                else:
                    configreset()
            else:
                with open('ajwlog.txt', 'w+') as log:
                    print("Couldn't find log path... creating 'ajwlog.txt'")
                    log.write('')
                    log.close()
                    checkline()
                
        except Exception:
            print(conferrinfo)

    #cmd system stuff
        if cmd == '>help':
            print('- >help.advanced        : Shows a list of more commands')
            print('- >clear                : Clear the screen')
            print('- >exit                 : Exit the command system')
            print('- >newcwd               : Change the current working directory (CWD)')
            print('- >ajwstatus            : Show current status about your AJW Command System')
            print('- >config               : AJW Command System config settings')
            print('- >credits              : Show the credits')

        elif cmd == '>help.advanced':
            #print('- >customscript         : Runs a custom script (Python only) made by you (customizable!)') ---> #removed for now, but still available for the python file version
            print('- >wincmd               : Runs a Windows command prompt command')
            print('- >print                : Print a text')
            print('- >hack                 : Be a HACKER MAN B) and hack a person')
            print('- >countluck            : Find out how lucky are you today ;)')
            print('- >date                 : Shows the current local date')
            print('- >time                 : Shows the current local time')
            print('- >randomtext           : Generate a random text')
            print('- >openprogram          : Open an external program')
            print('- >openweb              : Open a website via browser')
            print('- >pathlist             : Display list of contents of a specified path/folder')
            print('- >hexrgb               : Convert HEX code to RGB or vice versa')
            print('- >deletefile           : Deletes a spesific file')
            print('- >renamefile           : Renames a spesific file')
            print('- >calculator           : Calculator (tool to count)')
            print('- >rawfile              : Display what is inside of a file as a plain text')
            print('- >deletetemp           : Deletes Windows User temporary files')
            print('- >usageinfo            : Get current system usage info')
            print('- >wifispeed            : Get current Wifi download and upload speed')
            print('- >imgascii             : Turn an image into an ASCII art')
            print('- >playaudio            : Play an audio file')
            print('- >createtext           : Create a text file on a command shell based editor')
            print('- >translate            : Translate a language to another language (Google Translate API)')
            print('- >timer                : Allows you to set a timer on a spesific set of time')
            print('- >reactiontest         : Find out how fast you can react')
            print('- >countwords           : Count the total of words in a file')
            print('- >weatherinfo          : Weather information of a city')
            print('- >wikipedia            : Fetch a random or spesific wiki in Wikipedia')
            print('- >youtubedownloader    : Download a video from YouTube')
            print('- >createqr             : Generate a QR Code')
        
        elif cmd == '>credits':
            import colorama
            from colorama import Fore
            from colorama import init
            init(autoreset = True)
            
            print(Fore.YELLOW + f'AJW COMMAND SYSTEM - {version}')
            checkline()
            print(Fore.LIGHTYELLOW_EX + 'Made by Alexander Jason Wirawan')
            print(Fore.LIGHTYELLOW_EX + '2022')

        elif cmd == '':
            print("Please enter a command")

        elif cmd == '>newcwd':
            print("Current working directory is", workingdir)
            newcwd = input("New path: ")

            if newcwd == workingdir:
                print("Please enter a new path!")
            else:
                os.chdir(newcwd)
                workingdir = os.getcwd()
                print("Current working directory changed to", workingdir)
    
        elif cmd == '>exit':
            print("Exiting...")
            wait(2)
            print("You can exit the Shell now.")
            sys.exit()
            quit()

        elif cmd == '>clear':
            cls()
            if simplemode == 'simplemode=false\n':
                info()
            elif simplemode == 'simplemode=true\n':
                print('AJW Command System')
            else:
                configreset()
            
        elif cmd == '>wincmd':
            command = input("Enter CMD command: ")
            os.system(f'cmd /k {command}')
                
        elif cmd == '>print':
            text = input("Enter text: ")
            print(f"Printed text: {text}")
    
        elif cmd == '>hack':
            psw = ['Iam_Ugly73', 'pinkmaster_is_h3r3_reeee10', 'iamveryhandsome', 'you.are.reading.my.password', 'ohY3Slesg00', 'some_cool_dude52', 'insert:trollface_L0L']
            name = input("Enter name: ")
            platform = input("Platform name (Ex: YouTube): ")
            print(f"Getting {name}'s info on {platform}...")
            wait(2)
            print("Hashing password...")
            wait(2)
            print(f"Hacking {name}...")
            wait(2)
            print(f"{name} is succesfully hacked")
            print(f"> [ Password is '{random.choice(psw)}' ]")

        elif cmd == '>countluck':
            percent = range(100)
            luck = (random.choice(percent))
            print("How lucky are you today?")
            wait(1.5)
            print("Calculating...")
            wait(3)
            print(f"You are {luck}% lucky today!")

        elif cmd == '>date':
            from datetime import date
            today = date.today()
            day = today.strftime("%d/%m/%Y")
            print(f"DD/MM/YY: {day}")
        
        elif cmd == '>randomtext':
            import string
            import secrets 
            num = 10
            res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
            print("Generated Random Text: "+ str(res))

        elif cmd == '>openprogram':
            print("Note: If the program file is in the user folder, it might be unsupported")
            program = input("Program file location: ")
            subprocess.call([f'{program}'])
                
        elif cmd == '>openweb':
            import webbrowser
            site = input("Enter Website Adress: ")
            webbrowser.open(site)

        elif cmd == '>pathlist':
            from pathlib import Path
            path = input("Enter folder path: ")
            print(*Path(path).iterdir(), sep="\n")

        elif cmd == '>hexrgb':

            print("[1]HEX to RGB")
            print("[2]RGB to HEX")
            daoption = input("Enter choice: ")
            checkline()
            if daoption == '1':
                h = input('Enter HEX Code: ').lstrip('#')
                print('RGB Code =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

            elif daoption == '2':
                def clamp(x):
                    return max(0, min(x, 255))

                r=int(input("R: "))
                g=int(input("G: "))
                b=int(input("B: "))

                thehex=("#{0:02x}{1:02x}{2:02x}").format(clamp(r), clamp(g), clamp(b))
                print(thehex)

            else:
                print("Not an option!")

        elif cmd == '>deletefile':
            filepath = input("Enter File Path: ")
            os.remove(filepath)
            print("File successfully removed!")

        elif cmd == '>renamefile':
            old = input('File Path: ')
            new = input('New Name: ')
            os.rename(old, new)
            print("Success! (File can be found in the same folder as this program folder)")
            subprocess.Popen(f'explorer {workingdir}')

        elif cmd == '>calculator':
            a, b = [int(x) for x in input("Enter two numbers (x,y) = ").split(',')]
            operation=input("What do you wanna do? (+,-,*,/) = ")
            asr = "Answer: "

            if operation == '+':
                sum=a+b
                print(f"{asr}{sum}")
            elif operation == '-':
                sum=a-b
                print(f"{asr}{sum}")
            elif operation == '*':
                sum=a*b
                print(f"{asr}{sum}")
            elif operation == '/':
                sum=a/b
                print(f"{asr}{sum}")
            else:
                print("Sorry, there was an error calculating it")

        elif cmd == '>time':
            import datetime
            now = datetime.datetime.now()
            thetime = now.strftime("%H:%M:%S")
            print(f"HH:MM:SS: {thetime}")

        elif cmd == '>rawfile':
            name = input("File path: ")
            a_file = open(f"{name}")

            lines = a_file.readlines()
            for line in lines:
                print(line)

        elif cmd == '>deletetemp':    
            folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'
            deletedfiles = 0
            deletedfolders = 0

            for fname in os.listdir(folder):
                fpath = os.path.join(folder, fname)
                indxnum = fpath.find('\\')
                stuffName = fpath[indxnum+1:]
                try:
                    if os.path.isfile(fpath):
                        os.unlink(fpath)
                        print( '%s file is deleted' % stuffName )
                        deletedfiles = deletedfiles + 1

                    elif os.path.isdir(fpath):
                        if fpath.__contains__('chocolatey'):  continue
                        shutil.rmtree(fpath)
                        print( '%s folder is deleted' % stuffName )
                        deletedfolders = deletedfolders + 1

                except Exception as e:
                    pass
        
            checkline()
            print(str(deletedfiles)+' files and '+ str(deletedfolders)+' folders are successfully deleted.')

        elif cmd == '>usageinfo':
            import platform
            print(f'Device OS: {platform.system()} {platform.release()}')
            
            print("=====================CPU======================")
            print("Physical Cores        :",psutil.cpu_count(logical=False))
            print("Total Cores           :",psutil.cpu_count(logical=True))
            cpufreq = psutil.cpu_freq()
            print(f"Maximum CPU Frequency : {cpufreq.max:.2f}Mhz")
            print(f"Minimum CPU Frequency : {cpufreq.min:.2f}Mhz")
            print(f"Current CPU Frequency : {cpufreq.current:.2f}Mhz")
            for i,percentage in enumerate(psutil.cpu_percent(percpu=True,interval=1)):
                print(f"Core {i} Usage          : {percentage}%")
                
            print("=====================RAM======================")
            print('Total memory           : ', psutil.virtual_memory().total/(1000**3), 'GB')
            print('Available memory       : ', psutil.virtual_memory().available/(1000**3), 'GB')
            print('Current memory usage   : ', psutil.virtual_memory().percent, '%')

            print("=====================DISK=====================")
            total, used, free = shutil.disk_usage("/")
            print("Total disk space       : %d GB" % (total // (2**30)))
            print("Used disk space        : %d GB" % (used // (2**30)))
            print("Free disk space        : %d GB" % (free // (2**30)))


        elif cmd == '>wifispeed':
            import speedtest
            wifi  = speedtest.Speedtest()
            print("This may take a few seconds...")
            
            checkloading()
            checkline()
            
            print("Download Speed : ", wifi.download()/(1024*1024), "MB/s")
            print("Upload Speed   : ", wifi.upload()/(1024*1024), "MB/s")

        elif cmd == '>imgascii':
            print("Loading module, this may take a few seconds...")
            import pywhatkit
            
            checkloading()
            checkline()
            
            print("(Note: The result may not be very accurate compared to the image)")
            path = input('Image path: ')
            outputname = 'imgoutput'
            fulloutput = 'imgoutput.txt'
            pywhatkit.image_to_ascii_art(path, outputname)
            subprocess.Popen(["notepad.exe", fulloutput])

        elif cmd == '>playaudio':
            from playsound import playsound
            sound = input("Audio file location: ")
            playsound(sound)
      
        elif cmd == '>iwanttowalkaround': #easter egg 1
            cls()
            import keyboard

            def controls():
                print("--------------")
                print("[D] Go right")
                print("[A] Go left")
                print("[S] Stay")
                print("--------------")
            #char pos
            pos = 0
            char = ".('-')."
            char1 = ".(`-`)."
            char2 = ".(´-´)."

            #INTRO
            print()
            print(char)
            time.sleep(0.5)
            cls()
            print()
            print(char1)
            time.sleep(0.5)
            cls()
            print()
            print(char2)
            time.sleep(0.5)
            cls()
            print()
            print(char1)
            time.sleep(0.5)
            cls()
            print()
            print(char2)
            time.sleep(0.5)
            cls()
            print("Where to go?")
            print(char)
            time.sleep(0.2)
            controls()


            #magic begins
            while True:
                if keyboard.read_key() == "d":
                    cls()
                    pos=pos+1
                    currentpos = " " * pos
                    print("-> Going right")
                    print(currentpos, char1)
                    
                elif keyboard.read_key() == "a":
                    cls()
                    pos=pos-1
                    currentpos = " " * pos
                    print("<- Going left")
                    print(currentpos, char2)

                elif keyboard.read_key() == "s":
                    cls()
                    print("Ok, I will stay here")
                    print(currentpos, char)

        elif cmd == '>createtext':
            number = 1
            print("Type '<endeditor true>' to end the editor")
            buffer = []
            while True:
                print(str(number).zfill(3),"| ", end="")
                line = input()
                number=number+1
                if line == "<endeditor true>":
                    break
                buffer.append(line)
            contents = "\n".join(buffer)

            checkline()
            print("Preview:")
            print(contents)

            my_file = open("txtoutput.txt", "w")
            my_file.write(contents)
            my_file = open("txtoutput.txt")
            content = my_file.read()
            my_file.close()
            subprocess.Popen(["notepad.exe", "txtoutput.txt"])

        elif cmd == '>ajwstatus':
            process = psutil.Process(os.getpid())
            print(f"Current AJW Version      : {version}")
            checkline()
            
            if modded == 0:
                print("Current Modded Status    : False")
            elif modded == 1:
                print("Current Modded Status   : True")
                print(f"- Mod Name                : {modname}, created by {modauthor}")
                print(f"- Current Mod Version     : {modversion}")
            else:
                print("Modded Status   : Unspecified")

            pymemusage=psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
            checkline()
            print(f"Current AJW Memory Usage : {pymemusage} MB")

        elif cmd == '>translate':
            from googletrans import Translator, constants
            from pprint import pprint

            translator = Translator()
            print("[1] Auto translation")
            print("[2] Manual translation")
            option = input("Pick one: ")
            checkline()
            if option == "1":
                original = input("Enter a word: ")
                translation = translator.translate(original)
                checkline()
                print(f"{translation.origin} ({translation.src})")
                print(f"{translation.text} ({translation.dest})")

            elif option == "2":
                original = input("Enter a word         : ")
                newlang = input("Enter new language ID: ")
                translation = translator.translate(original, src=newlang)
                checkline()
                print(f"{translation.origin} ({translation.src})")
                print(f"{translation.text} ({translation.dest})")

            else:
                print("Not an option")

        elif cmd == '>timer':
            import datetime
            from playsound import playsound
            
            def countdown(h, m, s):

                total_seconds = h * 3600 + m * 60 + s

                while total_seconds > 0:
                    timer = datetime.timedelta(seconds = total_seconds)
                    print(timer, end="\r")
                    time.sleep(1)
                    total_seconds -= 1
             
                print("Time's up!!")

            try:
                h = input("Hours   : ")
                m = input("Minutes : ")
                s = input("Seconds : ")
                checkline()
                music = input("Ringtone file path (Optional): ")
                repeats = int(input("How many repeats             : "))
                checkline()
                countdown(int(h), int(m), int(s))
                for i in range(repeats):
                    playsound(music)
            except Exception:
                pass

        elif cmd == '>reactiontest':
            print("Press ENTER when another word pops up...")
            time.sleep(random.randint(1,4))
            then = time.time()
            checkline()
            t = input("PRESS ENTER NOW!")
            reactiontime = time.time()-then
            checkline()
            print(f"Your reaction speed is {reactiontime*1000:.0f} ms!")
            finalreaction = int(reactiontime*1000)

            if finalreaction in range(200, 300):
                print("GOOD!")

            elif finalreaction in range(90, 199):
                print("AMAZING!")

            elif finalreaction in range(0, 89):
                print("INHUMAN!")

            elif finalreaction in range(301, 600):
                print("SLOW!")

            else:
                print("VERY SLOW!")


        elif cmd == '>config':
            configfile = open("ajwconfig.txt", "r")
            read_conf = configfile.read()
            print("Preview:")
            print(read_conf)
            subprocess.Popen(["notepad.exe", "ajwconfig.txt"])
                        
        elif cmd == '>countwords':
            f = input("Enter file path: ")
            filename = open(f, 'r')
            readfile = filename.read()
            checkline()
            print("[1] Total words")
            print("[2] Total spesific words")
            option = input("Please choose: ")
            checkline()
            if option == "1":
                words = readfile.split()
                wordcount = int(len(words))
                if wordcount == 1:
                    print('There is 1 word in this file')
                else:
                    print('There are', wordcount, 'words in this file')
            elif option == "2":
                spesificword = input('Enter spesific word: ')
                wordcount = readfile.lower().count(spesificword)
                if wordcount == 1:
                    print(f"Found '{spesificword}' 1 time")
                else:
                    print(f"Found '{spesificword}' {wordcount} times")
            else:
                print('Not an option!')

                
        elif cmd == '>absolutelynothing': #easteregg 2
            with open('nothing.vbs', 'w+') as vbs:
                #vbs maker idk
                vbs.write('X=MsgBox("Do not click OK.",64)')
                def wshellrun():
                    vbs.write('\nSet WSHShell = WScript.CreateObject("WScript.Shell")')
                    vbs.write('\nWSHShell.Run "nothing.vbs"')
                wshellrun()
                wshellrun()
                vbs.close()
            filename = "nothing.vbs"
            programname = "wscript.exe"
            subprocess.Popen([programname, filename])
            print("=)")

        elif cmd == '>weatherinfo':
            from bs4 import BeautifulSoup
            import requests

            checkloading()
            checkline()

            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            def weather(city):
                    city = city.replace(" ", "+")
                    res = requests.get(
                            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    location = soup.select('#wob_loc')[0].getText().strip()
                    time = soup.select('#wob_dts')[0].getText().strip()
                    info = soup.select('#wob_dc')[0].getText().strip()
                    weather = soup.select('#wob_tm')[0].getText().strip()
                    
                    checkline()
                    print(location)
                    print(time)
                    print(info)
                    print(weather+"°C")

            city = input("City name: ")
            city = city+"weather"
            weather(city)


        elif cmd == '>wikipedia':
            print("Finding a topic...")
            import requests
            from bs4 import BeautifulSoup
            import webbrowser

            while True:
                url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
                soup = BeautifulSoup(url.content, "html.parser")
                title = soup.find(class_="firstHeading").text
                
                print(f"Topic: {title}")
                checkline()
                print('[1] Continue to random topic\n[2] Find another random topic\n[3] Go to a spesific topic\n[4] Exit')
                ans = input("Pick one: ").lower()
                checkline()
                if ans == "1":
                    url = "https://en.wikipedia.org/wiki/%s" % title
                    webbrowser.open(url)
                    print("Opening Wikipedia...")
                    break

                elif ans == "2":
                    print("Finding another topic...")
                    continue

                elif ans == "3":
                    spesific = input("Wiki title: ")
                    url = "https://en.wikipedia.org/wiki/%s" % spesific
                    print('Topic:',spesific)
                    webbrowser.open(url)
                    break
                    
                else:
                    print("Exiting...")
                    break

        elif cmd == '>customscript':#hidden for now
            print("Open 'customscript.py' to start editing your code! :)")
            checkline()
            custompath = 'customscript.py'
            cpath = Path(custompath)
                
            if cpath.is_file():
                open("customscript.py", "r")
                import customscript
                import importlib
                importlib.reload(customscript)
                customscript.customscript()
            else:
                print("couldn't find 'customscript.py'... creating file...")
                with open("customscript.py", "w") as custom:
                    custom.write("def customscript():\n#In this function, write your custom Python code.\n#-------------------------------\n#Do not delete this function\n    print('hi world!!')")
                    wait(1)
                    print("Done! (re-run this command)")
                    custom.close()


        elif cmd == '>youtubedownloader':
            from pytube import YouTube
            link = input("YouTube Video Link:  ")
            yt = YouTube(link)
            checkline()

            print("Video Title    : ",yt.title)
            print("Video Views    : ",yt.views)
            print("Video Duration : ",yt.length)
            checkline()

            ys = yt.streams.get_highest_resolution()
            print("Downloading file...")
            ys.download()
            print("Done!")
            print("(You can find the file in the same path as where you put AJW Command System in)")




        elif cmd == '>createqr':
            import qrcode
            import string
            import secrets 
            num = 4
            res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
            res = str(res)

            
            QRdata = input("Enter Website Adress: ")
            QRCodefile = f"{res}.png"
            QRimage = qrcode.make(QRdata)
            QRimage.save(QRCodefile)
            checkline()
            print(f"QR Code saved as '{QRCodefile}'")
            print("(You can find the file in the same path as where you put AJW Command System in)")

            

        else:
            #check simplemode
            if simplemode == 'simplemode=false\n':
                print(f'OOPS, the command "{cmd}" does not exist!')
            elif simplemode == 'simplemode=true\n':
                print('No existing command')
            else:
                pass

            #check enablelogging
            try:
                logpath = 'ajwlog.txt'
                zepath = Path(logpath)

                if zepath.is_file():
                    if enablelogging == 'enablelogging=false\n':
                        pass
                    
                    elif enablelogging == 'enablelogging=true\n':
                        with open('ajwlog.txt', 'r') as log:
                            before = log.read()
                            log.close()

                        with open('ajwlog.txt', 'w+') as log:
                            log.write(f"{before} [Invalid command]")
                            log.close()
                    else:
                        configreset()
                else:
                    with open('ajwlog.txt', 'w+') as log:
                        print("Couldn't find log path... creating 'ajwlog.txt'")
                        log.write('')
                        log.close()
                        checkline()

            except Exception:
                print(conferrinfo)

    except Exception:
        print("----------------------------------------------")
        print("Something is creating an error!")
        checkline()
        
        #check errorinfo
        if errorinfo == "errorinfo=true\n":
            print(sys.exc_info()[2])
            print()
            print(traceback.format_exc())
        elif errorinfo == "errorinfo=false\n":
            pass
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++")



        #check enablelogging
        try:
            logpath = 'ajwlog.txt'
            zepath = Path(logpath)

            if zepath.is_file():

                import datetime
                today = datetime.date.today()
                zday = today.strftime("%d/%m/%Y")
                
                now = datetime.datetime.now()
                ztime = now.strftime("%H:%M:%S")
                errexc = sys.exc_info()[2]
                
                if enablelogging == 'enablelogging=false\n':
                    pass
                
                elif enablelogging == 'enablelogging=true\n':
                    with open('ajwlog.txt', 'r') as log:
                        before = log.read()
                        log.close()

                    with open('ajwlog.txt', 'w+') as log:
                        log.write(f"{before}\n{zday} | {ztime} | Error {errexc}")
                        log.close()
                else:
                    configreset()
            else:
                with open('ajwlog.txt', 'w+') as log:
                    print("Couldn't find log path... creating 'ajwlog.txt'")
                    log.write('')
                    log.close()
                    checkline()
                
        except Exception:
            print(conferrinfo)
