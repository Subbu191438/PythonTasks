import random
import math
number = random.randint(1, 50)

attempts = 5

for i in range(attempts):
    guess = int(input("Enter your guess (1-50): "))
    difference = math.fabs(number - guess)
    
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Wrong guess!")
        print("You are", difference, "away from the correct number.")
        
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
else:
    print("Sorry! The correct number was:", number)
