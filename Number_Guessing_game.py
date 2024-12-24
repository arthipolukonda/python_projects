import random
import math
start,stop=map(int,input("enter start and stop values:").split())
Computernum=random.randint(start,stop)
num_of_guess=int(math.log(stop-(start+1),2))
for i in range(1,num_of_guess+1):
    if(i==num_of_guess):
        print("YOU HAVE ONLY ONE CHANCE")
    userguess=int(input("enter your number:"))
    if(Computernum==userguess):
        print(F"YOU WON!\n you guessed the number in {i} tries!")
        break;
    elif(Computernum>userguess and i!=num_of_guess):
        print("Try Again! You guessed too small")
    elif(Computernum<userguess and i!=num_of_guess):
        print("Try Again! You guessed too high")
    elif(Computernum>userguess or Computernum<userguess) and i==num_of_guess:
         print("YOU LOST! the number is",Computernum)
