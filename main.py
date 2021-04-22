# This is Apex V1.121, By: Elliott Hager, Rights & Credit goes to him for making Apex!!!!!
import time
one = 1
two = 2
three = 3
four = 4
five = 5
print ('Welcome To')
print (' ________  ________  _______      ___    ___ ')
print ('|\   __  \|\   __  \|\  ___ \    |\  \  /  /|')
print ('\ \  \|\  \ \  \|\  \ \   __/|   \ \  \/  / /')
print ('\ \   __  \ \   ____\ \  \_|/__   \ \   /  / ')
print (' \ \  \ \  \ \  \___|\ \  \_|\ \  /     \ /  ')
print ('  \ \__\ \__\ \__\    \ \_______\/  /\   \   ')
print ('   \|__|\|__|\|__|     \|_______/__/ /\ __\  ')
print ('                                |__|/ \|__|  ') 
time.sleep (2)
print ('What Can I do For You?')
print (' ')
print ('1.) Make a calculation')
print ('2.) Play a Game')
print ('3.) Chat')
print ('4.) ')
print ('5.) About')
number = float(input ('Number: '))
#
#Here is the Calculator Part of the Code, (Complete)
if number == one:
        a = 'a'
        b = 'b'
        c = 'c'
        d = 'd'
        print (' ')
        print (' ')
        print ('One it is!')
        print ('  ________  ________  ___       ________  ___  ___  ___       ________  _________  ________  ________       ')     
        print ('|\   ____\|\   __  \|\  \     |\   ____\ |\  \|\  \| \ \     |\   __  \|\___   ___\\   __  \|\   __  \      ')   
        print ('\ \  \___|\ \  \|\  \ \  \    \ \  \___| \ \  \\\  \  \ \    \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \     ') 
        print (' \ \  \    \ \   __  \ \  \    \ \  \     \ \  \\\  \  \ \    \ \   __  \   \ \  \ \ \  \\\  \ \   _  _\    ') 
        print ('  \ \  \____\ \  \ \  \ \  \____\ \  \____ \ \  \\\  \  \ \____\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \|   ')
        print ('   \ \_______\ \__\ \__\ \_______\ \_______ \ \_______\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\   ')
        print ('    \|_______|\|__|\|__|\|_______|\|_______| \|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|  ')
        number_one = float(input('Please give me the first number: '))
        print (' ')
        print (' ')
        number_two = float(input('Please give me the second number: '))
        print (' ')
        print (' ')
        print ('Avaible Opperators: ')
        print ('A.) Add')
        print ('B.) Subtract')
        print ('C.) Multiply')
        print ('D.) Divide')
        print (' ')
        operator = input('Please give me the opperation that you want to use: ')
        print (' ')
        if operator == a:
            print ('Your anwser is: ', number_one + number_two)
        if operator == b:
            print ('Your amwser is: ', number_one - number_two)
        if operator == c:
            print ('Your anwser is: ', number_one * number_two)
        if operator == d:
            print ('Your anwser is: ', number_one / number_two)
#
#Here is The Play Game Section of the Code (Work In Progress)
if number == two:
    print (' ')
    print ('________  ________  _____ ______   _______   ________    ')     
    print ('|\   ____\|\   __  \|\   _ \  _   \|\  ___ \ |\   ____\   ')     
    print ('\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|\ \  \___|_ ')   
    print (' \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/_\ \_____  \ ')  
    print (' \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \|____|\   \ ') 
    print ('  \ \_______\ \__\ \__\ \__\    \ \__\ \_______ \____\_\ \ ')
    print ('   \|_______|\|__|\|__|\|__|     \|__|\|_______|\_________\ ')
    print ('                                               \|_________| ')
#
#Here is the chat section of the Code (Work In Progress)
if number == three:
    
    print (' ')
    print (':) Lets Chat Then !')
    print ('......Loading.........')
    time.sleep (2)
    print ('Ready........So what do you want to talk about?')
    print ('Choices')
    print ('')
    first_chat_choice = float(input(''))
#
#Here is The About Section of the Code (Mostly Completed, Needs Work on the Return Function Though :/ )
if number == five:
    one_five = 'Y'
    changelog_five = 'Z'
    print (' ')
    print (' ')
    print ('Yay!, Let me get that information for you!')
    print ('Loading....')
    print ('  ________  ________  ________  ___  ___  _________    ')
    print (' |\   __  \|\   __  \|\   __  \|\  \|\  \|\___   ___\  ')
    print (' \ \  \|\  \ \  \|\ /\ \  \|\  \ \  \\\  \|___ \  \_|  ')
    print ('  \ \   __  \ \   __  \ \  \\\  \ \  \\\  \   \ \  \   ')
    print ('   \ \  \ \  \ \  \|\  \ \  \\\  \ \  \\\  \   \ \  \  ')
    print ('    \ \__\ \__\ \_______\ \_______\ \_______\   \ \__\ ')
    print ('     \|__|\|__|\|_______|\|_______|\|_______|    \|__| ')
    time.sleep (2)
    print (' ')
    print ('Apex is a digital assissitant that helps with basic tasks, such as calculations and more things to come in the ')
    print ('future. This is just a project for fun and to also to see what I know how to do in python, but to also learn  ')
    print ('more about the programming language. I am hoping to expand on the functions of Apex in the future, but for now ')
    print ('it is a basic calculator. :)')
    print (' ')
    print ('Apex Version: 0.1211, Updated: 11/11/2019, Created By: Elliott Hager ')
    print (' ')
    print ('For change log press Z and hit enter.')
    print (' ')
    choice_five = input(('Return to Main Menu?: '))
    if choice_five == 'Y':
        print (' ')
        print ('Okay... Let Me Load That For You....')
        print (' ')
        print ('Loading.......')
    if choice_five == 'Z':
        print (' ')
        print (' ')
        print ('Redirecting to update.... ')
        print (' ')
        print ('This is Version 1.1211')
        print (' ')
        print ('This version is the same as 1.121, just that')
        print (' this update is the only new thing added to ')
        print ('this version of APEX. I have been busy with ')
        print ('highschool, college, and band. I have not ')
        print ('forgotten this program though. I probally ')
        print (' will not update this anytime soon though')
        print (' ')
        print ('Thanks for checking out, and using Apex though!,')
        print ('Elliott Hager')
        print ('(The creator of Apex Digital Assitiant)')
        # end of redirected update!
        #
        #print ('This is Version 1.121 of Apex Digital Assitiant!')
        #print ('This version brings in the new chat feature, but it is')
        #print ('still buggy, I am working on making it more compact and')
        #print ('functional, The calculator has been done and it works fine')
        #print ('for basic opperations, but for more complicated tasks')
        #print ('it can not handle that. The games section still does not')
        #print ('have any funiction, because I am trying to figure out how')
        #print ('to add games to python with out PYGames or other graphical')
        #print ('layers and have it show straight up in the Pyhton Shell')
        #print ('Apex was built online on SoloLearn, and is running on')
        #print ('Python 3')
        #print ('Thank you for checking out Apex,')
        #print ('Elliott Hager')
        #print ('(The creator of Apex Digital Assisstant)')
        # NORMAL UPDATE ^^^^^^^^^^^^^^^^
    
    
