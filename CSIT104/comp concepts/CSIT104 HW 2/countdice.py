import random

def diceRoll(number): 
    rolls = []
    for i in range(0, number):
        rolls.append(random.randint(1, 6))
    return rolls

def commonSide(lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

results = diceRoll(50)
total = 0
for i in results:
    total += i 
print("Total: " +str(total)) 
print("Avgerage die value of all rolls: " +str(total / 50)) 
print("Rounded total: " +str(round(total / 50)))
print("Most frequent side of the die: " +str(commonSide(results)))

