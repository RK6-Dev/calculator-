from random import randint
def game():

 print( "GHOST  GAME" )
 print("==========================")
 score=0
 game_on= True

 while game_on:
    ghost_door = randint(1, 3)
    print("please choose a door")
    print("========================")
    door= input(' 1, 2 ,or 3: ')
    door_num = int(door)
    if door_num == ghost_door:
        print("there was a ghost")
        game_on= False

    else:
        print(' No ghost!' )
        print(' You enter the next room')
        score = score + 1
        print(' Your score is ', score)
 print(' RUN AWAY ')
 print(' YOU SCORED:', score)
def again():
     again = input("do u want to play again ? y/n")
     if again == 'y':
         game()
     elif again =='n':
         print("thank you for playing my game")
     else:
         print("invalid input")
game()