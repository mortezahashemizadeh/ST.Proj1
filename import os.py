import os
from time import sleep
import random 
os.system('cls')
print('WELCOME!!')
sleep(2)
os.system('cls')
#################################
def table (list):
    table = list
    print('   {}   |   {}   |   {}   '.format(table[0],table[1],table[2]))
    print("-------+-------+-------")
    print('   {}   |   {}   |   {}   '.format(table[3],table[4],table[5]))
    print("-------+-------+-------")
    print('   {}   |   {}   |   {}   '.format(table[6],table[7],table[8]))
def player_name ():
    name_list= [0, 0]
    name_list[0]= input("Palyer 1, Please enter your name: ")
    os.system('cls')
    name_list[1]= input("Player 2, Please enter your name: ")
    os.system('cls')
    return   name_list
def check_point(pos,s):  
    i = pos - 1
    if data[i] =='':
        data[i]=s
    else:
        print('Choose an other position')
        return True
def waiting(i):
    for _ in range(i):
        print('.')
        sleep(1)
        os.system('cls')
        print('..')
        sleep(1)
        os.system('cls')
        print('...')
        sleep(1)
        os.system('cls')

def result (list):
    if list[0]==list[1]==list[2]=='X' or list[0]==list[1]==list[2]=='O':
        return True
    elif list[3]==list[4]==list[5]=='X' or list[3]==list[4]==list[5]=='O':
        return True
    elif list[6]==list[7]==list[8]=='X' or list[6]==list[7]==list[8]=='O':
        return True
    elif list[0]==list[3]==list[6]=='X' or list[0]==list[3]==list[6]=='O':
        return True
    elif list[1]==list[4]==list[7]=='X' or list[1]==list[4]==list[7]=='O':
        return True
    elif list[2]==list[5]==list[8]=='X' or list[2]==list[5]==list[8]=='O':
        return True
    elif list[0]==list[4]==list[8]=='X' or list[0]==list[4]==list[8]=='O':
        return True
    elif list[2]==list[4]==list[6]=='X' or list[2]==list[4]==list[6]=='O':
        return True
    else:
        return False
def win():
    if result(data):
        print('play again? yes or no.')
        again = input('y/n?')
        if again == 'y':
            return True
        else:
            os.system('cls')
            print("GOOD LUCK!")
            sleep(2)
            os.system('cls')
            print ("--------------------------------------------------")
            print('coded by MORTEZA MOHAMMAD 2023')
            print ("--------------------------------------------------")
            sleep(2)
            exit()
##################################
waiting(2)
print("Let's Start Dooose Game!")
sleep(2)
os.system('cls')

name_list=player_name()
random.shuffle(name_list)
waiting(1)
print( name_list[0], " is O")
print(name_list[1], " is X")
sleep(3)
os.system('cls')
print ("--------------------------------------------------")

print('REMMEMBER POISTIONS OF CHOICE: ')

print ("--------------------------------------------------")

list_num = list(range(1,10))
table(list_num)
sleep(4)
os.system('cls')

waiting(1)
print(name_list[0],'START GAME',"\nLet's Go")
print ("--------------------------------------------------")
#####################preview of table########################

print('   {}   |   {}   |   {}   '.format("","",""))
print("------+------+-------")
print('   {}   |   {}   |   {}   '.format("","",""))
print("------+------+-------")
print('   {}   |   {}   |   {}   '.format("","",""))

#############################################################

""" print(name_list[0], "'s TURN")
choice = input("choose your position.")
choice= int (choice)
check_point(choice,'O')
os.system('cls')
table(data)

print(name_list[1], "'s TURN")
choice = input("choose your position.")
choice= int(choice)
check_point(choice,'X')
os.system('cls')
table(data) """
#def result (data):
data=['','','','','','','','','']
while True:

    #####user 1
    while True:
        print(name_list[0], "'s TURN")

        choice = input("choose your position: ")
        try:
                choice= int (choice)
        except:
                print('choose number between 1-9!!')
                continue
        if choice<=0 or choice>9:
            print('choose a number between 1-9')
            continue
       # check_point(choice,'O')
        if check_point(choice,'O'):
            continue
        os.system('cls')
        table(data)
        break
    if result(data):
        print("")
        print ("--------------------------------------------------")
        print(name_list[0],' is win.')
        print ("--------------------------------------------------")
    if win():
        data=['','','','','','','','','']
        os.system('cls')
        table(data)
        continue
    if not '' in data:
        print("")
        print ("--------------------------------------------------")
        print('No one is win!')
        print ("--------------------------------------------------")
        print('play again? yes or no.')
        again = input('y/n?')
        if again == 'y':
            os.system('cls')
            data=['','','','','','','','','']
            table(data)
            continue
        else:
            os.system('cls')
            waiting(2)
            print('GOOD BYE.')
            sleep(2)
            os.system('cls')
            print ("--------------------------------------------------")
            print('coded MORTEZA MOHAMMAD 2023')
            print ("--------------------------------------------------")
            break

    ####PLAYER 2
    while True:
        print(name_list[1], "'s TURN")
        choice = input("choose your position: ")
        choice= int (choice)
        if choice<=0 or choice>9:
            print('choose a number between 1-9')
            continue
       # check_point(choice,'X')
        if check_point(choice,'X'):
            continue
        os.system('cls')
        table(data)
        break
    if result(data):
        print("")
        print ("--------------------------------------------------")
        print(name_list[1],' is win.')
        print ("--------------------------------------------------")
    if win():
        data=['','','','','','','','','']
        os.system('cls')
        table(data)
        continue
    if not '' in data:
        print("")
        print ("--------------------------------------------------")
        print('No one is win!')
        print ("--------------------------------------------------")
        print('play again? yes or no.')
        again = input('y/n?')
        if again == 'y':
            os.system('cls')
            data=['','','','','','','','','']
            table(data)
            continue
        else:
            os.system('cls')
            waiting(2)
            print('GOOD BYE.')
            sleep(2)
            os.system('cls')
            print ("--------------------------------------------------")
            print('coded by MORTEZA MOHAMMAD 2023')
            print ("--------------------------------------------------")
            break


