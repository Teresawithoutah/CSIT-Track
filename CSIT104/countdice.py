import random

def rollDie(number): 
    rolls = []
    for i in range(0, number):
        rolls.append(random.randint(1, 6))
    return rolls

def most_common(lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

results = rollDie(50)
total = 0
for i in results:
    total += i 
print("Total: " +str(total)) 
print("Avg roll: " +str(total / 50)) 
print("Rounded total: " +str(round(total / 50)))
print("Most common: " +str(most_common(results)))

