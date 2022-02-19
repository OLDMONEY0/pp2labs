import random

name = input("Hello! What is your name?\n")
print ("Well, {}, I am thinking of a number between 1 and 20.".format(name))

randomnum = random.randint(1, 20)
give_num = int(input("Take a guess.\n"))
ch = 1

while give_num != randomnum:
    if give_num < randomnum:
        print ("Your guess is too low.")
    elif give_num >randomnum :
        print ("Your guess is too high.")
    give_num = int(input("Take a guess.\n"))
    ch += 1

print ("Good job, {}! You guessed my number in {} guesses!".format(name, ch))