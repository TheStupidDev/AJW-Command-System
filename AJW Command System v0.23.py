#basic setup
import traceback
import sys
import os
import subprocess
import time
import random
import shutil
import psutil
wait = time.sleep
workingdir = os.getcwd()

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

    print("Welcome to the AJW Command System (v0.23 BETA)!")
    print("Type >help to find out all the commands")

#unlooped stuff
info()


while True:
#looped stuff
    try:
    #basic program setup
        print("----------------------------------------------")
        cmd = input("Enter a command: ")
        print("----------------------------------------------")
    
    #cmd system stuff
        if cmd == '>help':
            print('- >help.advanced        : Shows a list of more commands')
            print('- >clear                : Clear the screen')
            print('- >exit                 : Exit the command system')
            print('- >credits              : Show the credits')

        elif cmd == '>help.advanced':
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
            print('- >hexrgb               : Convert HEX code to RGB of a color')
            print('- >deletefile           : Deletes a spesific file')
            print('- >renamefile           : Renames a spesific file')
            print('- >calculator           : Calculator (tool to count)')
            print('- >rawfile              : Display what is inside of a file as a plain text')
            print('- >deltemp              : Deletes Windows User temporary files')
            print('- >usageinfo            : Get current system usage info')
            print('- >wifispeed            : Get current Wifi download and upload speed')
            print('- >imgascii             : Turn an image into an ASCII art')
            print('- >playaudio            : Play an audio file')
        
        elif cmd == '>credits':
            print('Made by Alexander Jason Wirawan')
            print('2022')
    
        elif cmd == '>exit':
            print("Exiting...")
            wait(2)
            print("You can exit the Shell now.")
            sys.exit()
            quit()

        elif cmd == '>clear':
            def cls():
                os.system('cls' if os.name=='nt' else 'clear')
            cls()
            info()
            
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
            h = input('Enter HEX Code: ').lstrip('#')
            print('RGB Code =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

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
            time = now.strftime("%H:%M:%S")
            print(f"HH:MM:SS: {time}")

        elif cmd == '>rawfile':
            name = input("File path: ")
            a_file = open(f"{name}")

            lines = a_file.readlines()
            for line in lines:
                print(line)

        elif cmd == '>deltemp':    
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
        
            print("==============================================")
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
            print("==============================================")
            print("Download Speed : ", wifi.download()/(1024*1024), "MB/s")
            print("Upload Speed   : ", wifi.upload()/(1024*1024), "MB/s")

        elif cmd == '>imgascii':
            import pywhatkit
            print("(Note: The result may not be very accurate compared to the image")
            path = input('Image path: ')
            outputname = 'imgoutput'
            fulloutput = 'imgoutput.txt'
            pywhatkit.image_to_ascii_art(path, outputname)
            subprocess.Popen(["notepad.exe", fulloutput])

        elif cmd == '>playaudio':
            from playsound import playsound
            sound = input("Audio file location: ")
            playsound(sound)

        elif cmd == '>dontusethiscommand': #easter egg
            try:
                programname = "wscript.exe"
                filename = "Dont.Click.Me.vbs"
                subprocess.Popen([programname, filename])
                print("If there is an error, try these things:")
                print("- Download the file from https://bit.ly/3pt4Vfr")
                print("- After the file is downloaded, move the file into the same folder as this program")
                print("- Do not rename or edit the file to prevent errors")
            except Exception:
                print("There is an error!")
            
        else:
            print('Not a valid command')

    except Exception:
        print("----------------------------------------------")
        print("Error!")
        print(sys.exc_info()[2])
        print(traceback.format_exc())
