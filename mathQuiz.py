import random
import time

operators = ["+", "-", "*"]
minOp = 3
maxOp = 12
totalProb = 10


def generateProb():
    left = random.randint(minOp, maxOp)
    right = random.randint(minOp, maxOp)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!!!")
print("....................")

startTime = time.time()

for i in range(totalProb):
    expr, answer = generateProb()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

endTime = time.time()
totalTime = round(endTime - startTime, 2)

print("................")
print("You finished in", totalTime, "seconds! Congratulations!!")