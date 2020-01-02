import random

a = 1; b=9

number = random.randint(a,b)

def guessinggame(guess, numberofguesses):
    try:
      guessint = int(guess)
    except:
      raise RuntimeError("the guess could not be converted to int.")
    
    if guessint == number:
      print("correct! the number we picked is ", number)
      print("you guess correct in ", numberofguesses, "tries")
    if guessint < number:
      if input("that was too low :/ do you want to guess again?")[0] == "y":
        newguess = input("new guess?")
        numberofguesses += 1
        guessinggame(newguess, numberofguesses)
      else:
        print("the number was", number)
    
    if guessint > number:
      if input("that was too high :/ do you want to guess again?")[0] == "y":
        newguess = input("new guess?")
        numberofguesses += 1
        guessinggame(newguess, numberofguesses)
      else:
        print("the number was", number)

print("\n we have picked a number between ", a, " and ", b, ". \n now its your job to try and guess the number. \n")

guess = input("whats the guess?")

numberofguesses=1
guessinggame(guess, numberofguesses)
