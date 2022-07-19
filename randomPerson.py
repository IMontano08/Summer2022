from operator import truediv
import random

randomName = " "
peopleInRoom = []
def main():
    randomPick()
    loop1()
    

                        
def list():
    while True:
        try:
            n = int(input("Enter number of people in office: \n"))
        except ValueError:
            print("Make sure you only input numbers")
            continue
        break 
    
    print("Now enter their names (press enter after every name)")
    for i in range(0,n):
        people = str(input())
        peopleInRoom.append(people)
    print("\nYour list is: \n ")
    
def randomPick():
    print(peopleInRoom)
    print("Now picking one at random\n")
    global randomName 
    randomName = random.choice(peopleInRoom)
    print(str(randomName) +"\n") 
    
def remove():
    print(peopleInRoom)
    global randomName
    print("\nRemoving " + randomName  + " from list... \n")
    peopleInRoom.remove(randomName)


def finalMsg(): 
    print("\nHave fun at Lunch\n")

def loop1():
    loopCond = True;

    while loopCond == True and len(peopleInRoom) >= 2:
        
        x = input("Have another person pick? (Y/N)\n")
        if x.lower() == "y" or x.lower() == "yes":
            remove()
            randomPick()
        elif x.lower() == "n" or x.lower() == "no":
            loopCond = False
            finalMsg()
        else:
            print("Please select a valid option")
    finalMsg()
    
list()    
main()