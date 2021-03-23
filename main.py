import random
import keyboard

######################AUTHENETICATION############
password = "password"
players = "player1" or "player2"
access = True

while access:
    player = input("What is your username")
    if player != players:
        print("Incorrect username")
    
    if player == "player1":
        print("welcome player1")
    if player == "player2":
        pwinput = input("ENTER PASSWORD:")  
        if pw1input == password:
            print("access granted")
           
            access = True
            break   
   
    
# if pw1input != password:
#         print("Password Incorrect.")
#         access = True
        


# ##########################################

# rounds = 


# def dice(dice1, dice2):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)

# # player1Score = 
# # player2Score =

# player1prompt = print("Player 1")
# # if keyboard.is_pressed('space'):
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# total1 = dice1 + dice2
# print("You rolled a", dice1, "and a", dice2)
# print("your score is", total1)

# player1prompt = print("Player 2")
# # if keyboard.is_pressed('space'):
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# total2 = dice1 + dice2
# print("You rolled a", dice1, "and a", dice2)
# print("your score is", total2)

# player1prompt = print("Player 1")
# # if keyboard.is_pressed('space'):
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# total1 = total1 + dice1 + dice2
# print("You rolled a", dice1, "and a", dice2)
# print("your score is", total1)



# 1. Allows two players to enter their details, which are then authenticated to ensure that they are
# authorised players.
# 2. Allows each player to roll two 6-sided dice.
# 3. Calculates and outputs the points for each round and each player’s total score.
# 4. Allows the players to play 5 rounds.
# 5. If both players have the same score after 5 rounds, allows each player to roll 1 die each until
# someone wins.
# 6. Outputs who has won at the end of the 5 rounds.
# 7. Stores the winner’s score, and their name, in an external file.
# 8. Displays the score and player name of the top 5 winning scores from the external file.