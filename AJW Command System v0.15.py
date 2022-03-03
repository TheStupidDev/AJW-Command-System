#basic setup 1
import time
wait = time.sleep

#unlooped stuff
print("Welcome to the AJW Command System (v0.16 BETA)!")
print("Type >help to find out all the commands")

#looped stuff
while True:
    #basic program setup
    print("----------------------------------------------")
    cmd = input("Enter a command: ")
    print("----------------------------------------------")
    
    #cmd system stuff
    if cmd == '>help':
        print('- >credits              : Show the credits')
        print('- >exit                 : Exit the command system')
        print('- >print                : Print a text')
        print('- >hack                 : Hack a person')
        print('- >date                 : Shows the current date')
        print('- >random_text          : Generate a random text')
        print('- >open_program         : Open an external program')
        print('- >open_web             : Open a website')
        print('- >path_list            : Display list of contents in a folder/path')
        print('- >hex-rgb              : Convert HEX code of a color to RGB')
        print('- >delete_file          : Deletes a spesific file')
    
    elif cmd == '>credits':
        print('Made by Alexander Jason Wirawan')
        print('2022')
    
    elif cmd == '>exit':
        import sys
        print("Exiting...")
        wait(2)
        print("You can exit the Shell now.")
        sys.exit()
        quit()
    
    elif cmd == '>print':
        text = input("Enter text: ")
        print(f"Printed text: {text}")
    
    elif cmd == '>hack':
        name = input("Enter person who you wanna hack: ")
        print(f"hacking {name}...")
        wait(2)
        print(f"{name} is succesfully hacked")

    elif cmd == '>date':
        from datetime import date
        today = date.today()
        day = today.strftime("%d/%m/%Y")
        print(f"DD/MM/YY: {day}")
        
    elif cmd == '>random_text':
        import random
        import string
        import secrets 
        num = 10

        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
        print("Generated Random Text :"+ str(res))

    elif cmd == '>open_program':
        import subprocess
        print("Note: If the program file is in the user folder, it might be unsupported")
        program = input("Program file location: ")
        subprocess.call([f'{program}'])

    elif cmd == '>open_web':
        import webbrowser
        site = input("Enter Website Adress: ")
        webbrowser.open(site)

    elif cmd == '>path_list':
        from pathlib import Path
        path = input("Enter folder path: ")
        print(*Path(path).iterdir(), sep="\n")

    elif cmd == '>hex-rgb':
        h = input('Enter HEX Code: ').lstrip('#')
        print('RGB Code =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

    elif cmd == '>delete_file':
        import os
        filepath = input("Enter File Path = ")
        os.remove(filepath)
        print("File successfully removed!")
        
    else:
        print('Not a valid command')
