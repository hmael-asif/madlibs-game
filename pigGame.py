'''import random as random
turns=int(input("how many times would you like to roll the dice? "))
print("okay you have",turns,"turns")
score=0

for i in range (turns):
    roll=input("press any character to roll the dice: ")
    print("current turn: ",i+1)
    if(i==1):
        print("oops, you got a one, your score is now a 0")
        score=0
    else:
        roll=random.randint(1,6)
        print("you got: ",roll,"and your current score is: ", score+roll)
        score+=roll
    

print("your final score is: ",score) '''

import random as random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Enter the number of players (between 2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

maxScore = 50
playerScores = [0 for i in range(players)]

while max(playerScores) < maxScore:
    for playerNumber in range(players):
        print("\nPlayer number", playerNumber + 1, "turn: ")
        print("total score: ", playerScores[playerNumber], "\n")
        currentScore = 0

        while True:
            shouldRoll = input("Would you like to roll (y)? ")
            if shouldRoll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                currentScore = 0
                break
            else:
                currentScore += value
                print("You rolled a:", value)

            print("Score:", currentScore)

        playerScores[playerNumber] += currentScore
        print("Your total score is:", playerScores[playerNumber])

maxScore = max(playerScores)
winning = playerScores.index(maxScore)
print("Player number", winning + 1,
      "is the winner with a score of:", maxScore)