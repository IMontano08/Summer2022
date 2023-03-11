import random

Ogilvie=['Popeyes','Taco Bell','Panda Express','Arbys','Great Steak','Burrito Beach']
French=["Litos Empanada's",'Blue Spot Sushi',"Kathryn's Soul Food",'Jokers','Buen Appatito','Cubano Bros','Aloha Poke','Bangaroos','Saigon Sisters','Taste of Phillipines','Dim Sum']
Outside=['Avnti Cafe','Blaze Pizza','Chik Fil A','Epic Burger','Dog Haus','Asadito','Portillos','Blackies']

def Location():
    print('\n We going to eat somewhere at Ogilvie, French, or somewhere Outside?')
    Food = str(input("\n"))


def randomizer(Food):

    if Food == 'OGILVIE':
        print('\n'+random.choice(Ogilvie)+'\n')
    elif Food == 'FRENCH':
        print('\n'+random.choice(French)+'\n')
    elif Food == 'OUTSIDE':
        print('\n'+random.choice(Outside)+'\n')
    else:
        print('Wrong answer get it right next time!')
        Location()

def Reset():
    global Ogilvie
    global French
    global Outside
    Ogilvie=['Popeyes','Taco Bell','Panda Express','Arbys','Great Steak','Burrito Beach']
    French=["Litos Empanada's",'Blue Spot Sushi',"Kathryn's Soul Food",'Jokers','Buen Appatito','Cubano Bros','Aloha Poke','Bangaroos','Saigon Sisters','Taste of Phillipines','Dim Sum']
    Outside=['Avnti Cafe','Blaze Pizza','Chik Fil A','Epic Burger','Dog Haus','Asadito','Portillos','Blackies']

Location()

