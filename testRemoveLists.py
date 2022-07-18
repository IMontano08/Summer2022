import random

def main():
    list = []
    
    n = int(input("Enter number of people in office: \n"))
    print("Now enter their names (press enter after every name)")
    for i in range(0,n):
        people = str(input())
        list.append(people)
    print("Your list is: \n " + str(list))
    print("Now picking one at random")
    print(random.choice(list)+"\n") 
    #while len(list) > 03
       #list.remove(random.choice(list))
       #print(list)
        
main()
        