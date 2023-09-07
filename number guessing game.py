import random
import math

lower_bound = float(input("Enter the lower bound :- "))
upper_bound = int(input('Enter the upper bound :- '))
select_num = random.randint(lower_bound, upper_bound)
chance = round(math.log(upper_bound - lower_bound + 1 , 2))

print(f"You have {chance} chances to guess the number! ")

attempt = 0

while attempt < chance:
    attempt = attempt + 1

    x = int(input("Enter your guess :- "))

    if x == select_num:
        print(f"Congratulations! You have guessed correct number that is {select_num}")
        break
    elif x > select_num:
        print("You have guessed higher than actual value, Try to guess small :) ")
    elif x < select_num:
        print("You have guessed lower than actual value, Try to guess higher :) ")

if attempt >= math.log(upper_bound - lower_bound + 1, 2):
    print(f"\t\n\n The number is {select_num}")
    print("\t\n Better Luck Next time!")
