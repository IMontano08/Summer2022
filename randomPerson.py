from operator import truediv
import random

randomName = " "

def main():
    list()
    randomPick()
    loop1()
    

                        
def list():
    peopleInRoom = []
    n = int(input("Enter number of people in office: \n"))
    print("Now enter their names (press enter after every name)")
    for i in range(0,n):
        people = str(input())
        list.append(people)
    print("\nYour list is: \n " + str(list))
    
def randomPick():
    print("Now picking one at random\n")
    randomName = random.choice(list)
    print(str(randomName) +"\n") 
    
def remove():
    list.remove(randomName)

def loop1():
    loopCond = True
    while loopCond == True:
        x = input("Have another person pick? (Y/N)")
        x = x.upper()
        if x == "Y" | "YES":
            remove()
            randomPick()
            
        
        

def loop2():

def loop3(): 
    
def finalMsg():          
            
        
        
        
    
    
main()