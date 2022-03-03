#basic setup
import traceback
import sys
import os
import time
import random
wait = time.sleep

#unlooped stuff
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

print("Welcome to the AJW Command System (v0.19 BETA)!")
print("Type >help to find out all the commands")

while True:
#looped stuff
    try:
    #basic program setup
        print("----------------------------------------------")
        cmd = input("Enter a command: ")
        print("----------------------------------------------")
    
    #cmd system stuff
        if cmd == '>help':
            print('- >credits              : Show the credits')
            print('- >exit                 : Exit the command system')
            print('- >help.advanced        : Shows a list of more commands')
            
        elif cmd == '>help.advanced':
            print('- >wincmd               : Runs a window command prompt command')
            print('- >print                : Print a text')
            print('- >hack                 : Be a HACKER MAN B) and hack a person')
            print('- >countluck            : Find out how lucky are you today ;)')
            print('- >date                 : Shows the current local date')
            print('- >time                 : Shows the current local time')
            print('- >randomtext           : Generate a random text')
            print('- >openprogram          : Open an external program')
            print('- >openweb              : Open a website via browser')
            print('- >pathlist             : Display list of contents of a specified path/folder')
            print('- >hexrgb               : Convert HEX code of a color to RGB')
            print('- >deletefile           : Deletes a spesific file')
            print('- >renamefile           : Renames a spesific file')
            print('- >calculator           : Calculator (tool to count)')
            print('- >rawfile              : Display what is inside of a file as a plain text')
        
        elif cmd == '>credits':
            print('Made by Alexander Jason Wirawan')
            print('2022')
    
        elif cmd == '>exit':
            print("Exiting...")
            wait(2)
            print("You can exit the Shell now.")
            sys.exit()
            quit()

        elif cmd == '>wincmd':
            command = input("Enter CMD command: ")
            os.system(f'cmd /k {command}')
                
        elif cmd == '>print':
            text = input("Enter text: ")
            print(f"Printed text: {text}")
    
        elif cmd == '>hack':
            psw = ['Iam_Ugly73', 'pinkmaster_is_h3r3_reeee10', 'iamveryhandsome', 'you.are.reading.my.password', 'ohY3Slesg00', 'some_cool_dude52', 'insert:trollface_L0L']
            name = input("Enter name: ")
            input("Platform name (Ex: Youtube): ")
            print(f"Getting {name}'s info...")
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
            import subprocess
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
            print("Success! (You can find the file in the folder you place this program on) ")

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
            name = input("File name: ")
            a_file = open(f"{name}")

            lines = a_file.readlines()
            for line in lines:
                print(line)

        else:
            print('Not a valid command')

    except Exception:
        print("----------------------------------------------")
        print("Error!")
        print(sys.exc_info()[2])
        print(traceback.format_exc())
