import random

n = int(input("Please enter a number: "))
p = int(input("Please enter the number of players: "))

players = ["James"]
scores = [0]

for i in range(p):
    ask = input("What is your name Player " + str(i+1) + "?: ")
    if i == 0:
        players[0] = ask
    else:
        players.append(ask)
    print("Starting the game for", players[i])
    counter = 0
    guessed = False
    x = random.randint(0,n)
    while guessed == False:
        guess = int(input("Enter your guess: "))
        if guess > x:
            print("Too large")
        elif guess < x:
            print("Too small")
        counter = counter + 1
        if guess == x:
            print("You guessed it right with " + str(counter), "guesses")
            if i == 0:
                scores[0] = counter
            else:
                scores.append(counter)
            guessed = True

least = scores[0]
winners = 0
for i in range(len(players)):
    if scores[i] < least:
        least = scores[i]

for i in range(len(players)):
    if least == scores[i]:
        winners = winners + 1
        if (winners > 1):
            print(",", end = " ")
        print(players[i], end = "")   

if winners > 1:
    print("are winners.")
else:
    print("is the winner.")