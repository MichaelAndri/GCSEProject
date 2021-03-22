import random
import keyboard

######################AUTHENETICATION############
p1password = "password1"
p2password = "password2"

print("Please enter credentials player1")
password = input("ENTER PASSWORD:")
access = False
for access == False:
    if password == p1password:
        print("Welcome Player 1")
        access = True
    else:
        print("Password Incorrect.")
        password("TRY AGAIN")

print("Please enter credentials player2")
password = input("ENTERPASSWORD:")
##########################################




# 1dieA = random.randint(1,6)
# 1dieB = random.randint(1,6)
# 2dieA = random.randint(1,6)
# 2dieB = random.randint(1,6)

# player1Score = 1dieA+1dieB
# player2Score = 2dieA+2dieB

# player1prompt = print("Player 1 please press space to roll")
# if keyboard.is_pressed('space'):
#     print("You rolled a", die1)




#  Design, develop, test and evaluate a system that:
# 1. Allows a player to enter their details, which are then authenticated to ensure that they are an
# authorised player.
# 2. Stores a list of song names and artists in an external file.
# 3. Selects a song from the file, displaying the artist and the first letter of each word of the song title.
# 4. Allows the user up to two chances to guess the name of the song, stopping the game if they guess
# a song incorrectly on the second chance.
# 5. If the guess is correct, add the points to the player’s score depending on the number of guesses.
# 6. Displays the number of points the player has when the game ends.
# 7. Stores the name of the player and their score in an external file.
# 8. Displays the score and player name of the top 5 winning scores from the external file.