import random

def codeMaker(a):#make the code to be cracked from the colours array
  puzzle = []
  while len(puzzle) < 4:
    x = random.randint(0,len(a)-1)
    if a[x] not in puzzle:
      puzzle.append(a[x])
  return puzzle

def checker(array, p, user):#checks for penalties and issues them. This function takes: (guess, penalty, playername)
  penaltyIssued = False
  error1 = False#error1 is the error of a repeated colour
  error2 = False#error2 is the error of a colour not in the list
  error3 = False#error3 is the error of an incorrect amount of guesses

  upperColours = colours#this is done for the function that checks misspelt colours or colours that aren't in the list
  for i in range(len(colours)):
    upperColours[i] = upperColours[i].upper()

  if len(array) != 4:#checks if there are any amount of guesses other than 4 made
    error3 = True
    penaltyIssued = True

  i = 0
  while i < len(array):#checks for the penalty of a repeated colour
    for j in range(len(array)):
      if i != j:
        if array[i].upper() == array[j].upper():
          error1 = True
          penaltyIssued = True
          i = len(array) + 1
          break
    i = i + 1

  i = 0
  while i < len(array):#checks for the penalty of a misspelt colour or a colour that isn't in the list
    if array[i].upper() != " " and array[i].upper() not in upperColours:
      error2 = True
      penaltyIssued = True
      i = len(array) + 1
    i = i + 1

  if penaltyIssued == True:
    p = p + 1
    print("Sorry", user, end = ".")
    if error1 == True:
      print(" Repeated colours are not allowed in this game.", end = "")
    if error2 == True:
      print(" Cannot recognize the colours you entered.", end = "")
    if error3 == True:
      print(" You need to enter at least 4 colours for each guess.", end = "")
    print(" One penalty is considered.")
      
  return penaltyIssued, p  

def codeGuesser(response, puzzle, user):#Check the guess to see how many whites and blacks the player gets. The function takes (guess, code, playername)
  victory = False
  b = 0
  w = 0

  upperCode = code
  for i in range(len(code)):
    upperCode[i] = upperCode[i].upper()
      
  for i in range(len(response)):
    if response[i].upper() == puzzle[i].upper():
      b = b + 1
    elif response[i].upper() in puzzle:
      w = w + 1
  if b != 4:
    print("You got", b, "blacks and", w, "whites for this guess.")
  else:
    print("You got 4 blacks " + user + ".")
    victory = True
  return victory

#begin the main code:

colours = ["Red", "Yellow", "Blue", "Green", "Orange", "Pink", "Purple", "Cyan", "Silver", "Teal"]
penalty = 0
gameWon = False

code = codeMaker(colours)

playername = input("What is your name?: ")
print("Welcome to Master Mind " + playername + "!")

knowledge = input("Do you know how to play?(input y if yes): ")#asks if the user wants to know how to play the game
if knowledge.lower() != 'y':
  print("It seems as though you would like to know how to play Master Mind. Here are the rules: ")
  print("The object of the game is to guess a 4 colour code with the amount of guesses you have.")
  print()
  print("You will be told after each guess that amount of whites and blacks that you get. A white means that you have correctly guessed a colour in the code, but it isn't in the correct position. A black on the other hand, means that you have correctly guessed a colour in the code, and it is in the correct position.")
  print()
  print("It is important to note that if you guess the same colour twice, don't enter 4 guesses, guess with commas, misspell a colour, or guess a colour not in the list, you will receive a penalty.")
  print()
  print("Now, the game will begin.")
  print()

print("The code maker is here. Available colours are: ")
for i in range(len(colours)):
  if i + 1 != len(colours):
    print(colours[i], end = ", ")
  else:
    print(colours[i])
print()
print("You have 15 guesses and a total of 5 penalties are allowed, but avoid penalties.")
print("The code maker has selected 4 colours.")
print("You can start guessing " + playername + ".")

i = 1
while i < 16:
  print()
  mistakeMade = False
  guess = input("Enter guess number " + str(i)  + ": ")
  guess = guess.split(" ")
  mistakeMade, penalty = checker(guess, penalty, playername)
  if mistakeMade == True:
    continue
  gameWon = codeGuesser(guess, code, playername)
  if gameWon == True:
    break
  i = i + 1

if gameWon == True:
  print("You won the game with", i, "guesses and", penalty, "penalties, Congratulations.")
if i > 15:
  print("Sorry", playername, ", you ran out of guesses and lost the game with", penalty, "penalties.")
