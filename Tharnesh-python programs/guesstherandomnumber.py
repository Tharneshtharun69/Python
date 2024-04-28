import random
def guess_randomnum():
    score = 0
    while True:
        num = random.randint(1, 6)
        guess = int(input("Enter your guess: "))
        if num == guess:
            score += 1
            print("Hurrah! You've guessed the number correctly")
            print("Your score is:", score)
        else:
            score -= 1
            print("Alas! It's a wrong number")
            print("The correct number was:", num)
            print("Your score is:", score)
guess_randomnum()
