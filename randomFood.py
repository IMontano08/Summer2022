import random

OGILVIE=['Popeyes','Taco Bell','Panda Express','Arbys','Great Steak','Burrito Beach']
FRENCH=["Litos Empanada's",'Blue Spot Sushi',"Kathryn's Soul Food",'Jokers','Buen Appatito','Cubano Bros','Aloha Poke','Bangaroos','Saigon Sisters','Taste of Phillipines','Dim Sum']
OUTSIDE=['Avnti Cafe','Blaze Pizza','Chik Fil A','Epic Burger','Dog Haus','Asadito','Portillos','Blackies']

global randomPick 
global Food #global variables for randomPick and Food

def Reset():
    global OGILVIE
    global FRENCH
    global OUTSIDE
    OGILVIE=['Popeyes','Taco Bell','Panda Express','Arbys','Great Steak','Burrito Beach']
    FRENCH=["Litos Empanada's",'Blue Spot Sushi',"Kathryn's Soul Food",'Jokers','Buen Appatito','Cubano Bros','Aloha Poke','Bangaroos','Saigon Sisters','Taste of Phillipines','Dim Sum']
    OUTSIDE=['Avnti Cafe','Blaze Pizza','Chik Fil A','Epic Burger','Dog Haus','Asadito','Portillos','Blackies']

def Location():
    global Food
    Food = input('We going to eat somewhere at Ogilvie, French, or somewhere Outside?\n') #prompt user for location, repeats back after asking if user wants to try again
    if len(Food.upper()) == 0: #not working atm, not sure why
        Reset()
    randomizer(Food)

def randomizer(Food):
    global randomPick
    print("Now randomly selecting from " + Food.upper() + "...")    #randomly select from OGILVIE, French, or Outside
    if Food.upper() == 'OGILVIE':
        randomPick = random.choice(OGILVIE)        #announce what randomPick is
    elif Food.upper() == 'FRENCH':
        randomPick = random.choice(FRENCH)
        print('\n'+randomPick+'\n')
    elif Food.upper() == 'OUTSIDE':
       randomPick = random.choice(OUTSIDE)
       print('\n'+randomPick +'\n')
    else:
        print('Wrong answer get it right next time!')
        Location()

def remove(randomPick):
    print("\nNow removing " + randomPick + " from " + Food.upper() + "...")     #in case user is not satisfied with randomPick, remove it from OGILVIE, French, or Outside
    if Food.upper() == 'OGILVIE':   
        OGILVIE.remove(randomPick)
        print("The size of Ogilvie is " + str(len(OGILVIE)) + ".\n")            #print size of OGILVIE, french, or Outside after removing randomPick to make sure it's removed
    elif Food.upper() == 'FRENCH':
        FRENCH.remove(randomPick)
        print("The size of French is " + str(len(FRENCH)) + ".\n")
    elif Food.upper() == 'OUTSIDE':
        OUTSIDE.remove(randomPick)
        print("The size of Outside is " + str(len(OUTSIDE)) + ".\n")

def differentOption():
    loopCond = True  

    while loopCond == True:
        again = input("Would you like to try again?(Y/N)")              #loop condition asking if user wants to try again
        if again.lower() == 'y':
            remove(randomPick)
            Location()
        elif again.lower() == 'n':
            print("Have fun at lunch!")
            loopCond = False
        else:
            print("Please select a valid option!")

Location()
differentOption()
