import random

print("This is an interactive guessing game!")
print("You have to enter a number between \
1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()

i = random.randint(1, 99)
a = 1
while (1):
    inp = input("What's your guess between 1 and 99?\n")
    if inp == "exit":
        print("Goodbye!")
        break
    elif inp.isdigit() is not True:
        print("That's not a number.")
    elif int(inp) == i:
        if a == 1:
            if i == 42:
                print("The answer to the ultimate question of life, \
the universe and everything is 42.")
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in", a, "attempts!")
        break
    elif (int(inp) > i):
        print("Too high!")
    elif (int(inp) < i):
        print("Too low!")
    a += 1
