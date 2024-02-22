'''This is a Rock Papper scissor Game '''

# importing the random module
import random
print('***************welocme to Rock Papper Scissor Game***************\n')
print('winning Rules of the Rock paper and scissor game as follows:\n'
    + 'rock vs paper->paper wins\n'
    + 'rock vs scissors->rock wins\n'
    + 'paper vs scissors->scissors wins\n')

while True:
    print("Enter Your Choice:\n 1. Rock\n 2. Papper\n 3. Scissor")

    # Take input from user
    choice=int(input("Enter your Choice:"))

    while choice > 3 or choice < 1:
        print("Enter a Valid choice please...😊😊😊")
    
    match choice:
        case 1:
            choice_name='Rock'
        case 2:
            choice_name='Papper'
        case 3:
            choice_name='Scissor'

    print(f'User Choice : {choice_name}\n')

    print('Now its Ai Turn ....😉😉')

    ai_choice=random.randint(1,3)

    # while ai_choice==choice:
    #     ai_choice=random.randint(1,3)

    match ai_choice:
        case 1:
            ai_choice_name='Rock'
        case 2:
            ai_choice_name='Papper'
        case 3:
            ai_choice_name='Scissor'

    print(f'Ai choice is {ai_choice_name}\n')

    print(choice_name,'Vs',ai_choice_name)

    # check for draw
    if choice==ai_choice:
        result='Draw'

    # winning condition
    if choice==1 and ai_choice==2 or ai_choice==1 and choice==2:
        print('Papper wins==>',end=' ')
        result='Papper  '
    elif choice==1 and ai_choice==3 or ai_choice==1 and choice==3:
        print('Rock wins==>',end=' ')
        result='Rock'
    elif choice==2 and ai_choice==3 or ai_choice==2 and choice==3:
            print('Scissor wins==>',end=' ')
            result='Scissor'
    
    if result=='Draw':
        print('its a Tie==========>')
    elif result==choice_name:
        print('User wins==========>')
    else:
        print('Computer wins==========>')
    # play again 
        
    print('Do you want to play again:(Y/N)')
    if input().lower()=='n':
        break
print("Thanksfor palying the game")
