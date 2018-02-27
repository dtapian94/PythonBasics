#Daniel Tapia Nava
#February 2018

from random import randint

min = 1
max = 6


print("This will be a program to simulate a rolling dice")

repeat = True

while repeat:
    print("You rolled : ",randint(min,max) , "and ", randint(min,max))
    
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()




