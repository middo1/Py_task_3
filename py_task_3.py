#-*-coding:utf8;-*-
#qpy:console

import random

# processes the guessed number 
def guesspro(num, limit):
    rnum = random.randint(1, limit)
    if rnum == num:
        return True
    else:
        return False

level = input("Enter desired level i.e easy, medium or hard: ") 
 
while True:
    if level == "easy" :
        tries = 5
        lim = 11
        guess = int(input("Enter your guess from the range of 1 to " + str(lim - 1) + ": "))
        while tries > 0:
            res = guesspro(guess, lim)
            if res == True:
                print("You guessed it right") 
                break
            else:
                print("Your guess is wrong please try again") 
                tries -= 1
                guess = int(input("Enter your guess from the range of 1 to " + str(lim - 1) + ": "))
                if tries == 0 and res == False:
                    print("You have used up your chances to guess")
                    break
        break
    elif level == "medium" :
        tries = 3
        lim = 21
        guess = int(input("Enter your guess from the range of 1 to " + str(lim - 1) + ": "))
        while tries > 0:
            res = guesspro(guess, lim)
            if res == True:
                print("You guessed it right") 
                break
            else:
                print("Your guess is wrong please try again") 
                tries -= 1
                guess = int(input("Enter your guess from the range of 1 to " + str(lim - 1) + ": "))
                if tries == 0 and res == False:
                    print("You have used up your chances to guess")
                    break
        break
    elif level == "hard" :
        tries = 2
        lim = 51
        guess = int(input("Enter your guess from the range of 1 to " + str(lim - 1) + ": "))
        while tries > 0:
            res = guesspro(guess, lim)
            if res == True:
                print("You guessed it right") 
                break
            else:
                print("Your guess is wrong please try again") 
                tries -= 1
                guess = int(input("Enter your guess from the range of 1 to " + str(lim - 1) + ": "))
                if tries == 0 and res == False:
                    print("You have used up your chances to guess")
                    break
        break
    else:
        level = input("Please enter required level like easy, medium, hard : ")


