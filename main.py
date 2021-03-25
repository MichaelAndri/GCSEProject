import random
import time

######################AUTHENETICATION############
password = "password"
players = "player1" or "player2"
Player1Points = 0
Player2Points = 0
Player1Tiebreaker = 0
Player2Tiebreaker = 0

def login():
    while True:
        username = input("What is your username")
        password = input("What is your password")
        if username != players:
            print("Incorrect username. Please try again")
            continue

        if password != 'password':
            print("Incorrect password. Please try again")
            continue

        print(f'Welcome, {username} you have been logged in.')
        return username

print("Player 1 please login.")
login()
print("player 2 please login.")
login()

#  if player == "player1":
#             print("welcome player1")
#             pwi = input("Player1 please enter your password")
#             if pwi == password:
#                 print("access granted")
#                 access = True

#         if player == "player2":
#             print("welcome player2")
#             pwi = input("Player2 please enter your password")
#             if pwi == password:
#                 print("access granted")    
#                 access = False

       
#########  ROLLS DICE AND WORKS OUT TOTAL FOR THAT ROLL###############


def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    change = 10 if (dice1+dice2) % 2 == 0 else -5
    points = dice1 + dice2 + change
    if dice1 == dice2:
        points += random.randint(1,6)
    return points

for i in range(1,5):
    Player1Points += roll()
    print(f'After this round player1 you now have: {Player1Points} Points')
    time.sleep(1)
    Player2Points += roll()
    print(f'After this round player2 you now have: {Player2Points} Points')
    time.sleep(1)

#########  TIEBREAKER  ###################

if Player1Points == Player2Points:
    while True:
        Player1Tiebreaker = random.randint(1,6)
        Player2Tiebreaker = random.randint(1,6)

    if Player1Tiebreaker > Player2Tiebreaker:
        Player2Points = 0
    elif Player2Tiebreaker > Player1Tiebreaker:
        Player1Points = 0 

############# WINNER #####################



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