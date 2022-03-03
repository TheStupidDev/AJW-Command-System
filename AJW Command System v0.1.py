#setup 1
import time
wait = time.sleep

#basic program setup
print("Type >help to find out all the commands")
cmd = input("Enter a command: ")

#cmd system stuff
if cmd == '>help':
    print('- >print : Print a text')
    print('- >hack  : Hack a person')
    print('- >date  : Shows the date today')

elif cmd == '>print':
    text = input("Enter text:")
    print(text)
    
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
   
else:
    print('Not a valid command')
