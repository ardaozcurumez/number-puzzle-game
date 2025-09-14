import time
import random

flag1 = "continue"
flag2 = "GO"

print("Welcome to NUMBER PUZZLE GAME!")
time.sleep(2)

option2 = input("if you are ready type \"GO\" to play. : ").upper()

while True:
    
    if option2 == flag2:
        break
    else:
        option2 = input("Wrong key word to play! Try again. : ").upper()


while flag1 == "continue":
    
    time.sleep(1.5)
    print("\nWhen the countdown ends, the timer starts!\n")
    time.sleep(2)
    print("3..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    time.sleep(1)

    print("-----------------------------------------")
    
    number = random.randint(1,100)

    starting_time = time.time()

    guess = int(input("\nMake a guess! : "))
    print("\n")

    attempt = 1

    if guess != number:
        
        while guess != number:

            if guess < number:

                print("Your guess lower than the number!\n")
                guess = int(input("Try again! : "))
                print("\n-----------------------------------------\n")
                attempt+=1
                continue

            elif guess > number:
                
                print("Your guess bigger than the number!\n")
                guess = int(input("Try again! : "))
                print("\n-----------------------------------------\n")
                attempt+=1
                continue
    
    
    print("Well Done! You find it.\n")
    finishing_time = time.time()
    finding_time = finishing_time - starting_time   

    print("Result -->\n")     
    print("*****************************************\n")
    print(f"Hidden Number: {number}\n")
    print(f"Your Attempts: {attempt}\n")
    print(f"Finding Time: {finding_time:.2f} seconds\n")
    print("*****************************************\n")

    time.sleep(2)

    option1 = input("Write \"continue\" to play or \"stop\" to exit: ").lower()
    
    if option1 != "continue":
        print("Thanks for playing! 👋")
        break
