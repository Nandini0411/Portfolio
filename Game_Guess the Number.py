The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

#importing Library
from random import randint

#taking a random number
guess_num=randint(1,100)
guess_num


# initializing variables and list
num=0
compare_num=0
mylist=[]
num=int(input("Enter a number:"))
mylist.append(num)
#Checking for the first pass
if(num<0 or num>100):
    print("OUT OF BOUND")
else:
    diff=num-guess_num
    if(diff==0):
        print("Eureka!!! You found it")
    elif(diff<-10 or diff>10):
        print("Cold")
    else:
        print("Warm")

#Comparing for the subsequent passes
while(num!=guess_num):
    compare_num=mylist[-1]
    num=int(input("Enter a number:"))
    mylist.append(num)
    if(num<0 or num>100):
        print("OUT OF BOUND")
    else:
        diff1=num-guess_num
        diff2=compare_num-guess_num
        if(diff1==0):
            print("Eureka!!! You found it")
        elif(abs(diff2)<abs(diff1)):
            print("Colder")
        else:
            print("Warmer")
        
        

print(mylist)

no_of_guesses=len(mylist)
print(f"It took you {no_of_guesses} guesses to get to the number ")