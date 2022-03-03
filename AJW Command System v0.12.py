#setup 1
import time
wait = time.sleep
print("Welcome to the AJW Command System!")
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
        print('- >print                : Print a text')
        print('- >hack                 : Hack a person')
        print('- >date                 : Shows the current date')
        print('- >generate_random_text : Generate a random text')
    
    elif cmd == '>credits':
        print('Made by Alexander Jason Wirawan')
        print('2022')
    
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
        
    elif cmd == '>generate_random_text':
        import random   
        import string  
        import secrets  
        num = 10

        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
        print("Generated Random Text :"+ str(res))  
        
    else:
        print('Not a valid command')