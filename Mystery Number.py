import random
num = random.randint(1,100)
guessNum = 1
while(True):
    guess = int(input("\nEnter your guess in range 1 to 100: "))
    if(guessNum == 5):
        print(f"\nMaximum Tries achieved!. The number was {num}")
        break
    if(guess != num):
        guessNum+=1
    if(guess - num == 0):
        print("\nGreat! you selected the right option")
        print(f"\nThe number of guesses you took are {guessNum}")
        break
    elif(guess!=num and guess - num > 35):
        print("\nDifference is too much, Try again")
    elif(guess!=num and guess - num < 35):
        print("\nNice Try, Now Difference is less")