import random

print ("Welcome! Let's play a game! You have five chances to guess the word I pick. Goodluck!")
words = ['money','fame','fortune','riches','death','pain','hell','heaven','devil','god','seraphine','phone','technology','programming','computer','ethics','morality','philosophy','scamming','education','nothing','matters','anymore']
word = random.choice(words)
print ("The password is", len(word), "letters long.")
guesscount = 0
while guesscount <= 4:
    guesscount += 1
    guess = input("guess a letter: ")
    if guess in word:
        print ("yes")
    elif guess not in word:
        print ("no")
    elif guess == " ":
        print ("no")
print ("You are out of tries, guess the word!")
guess_word = input("Input code: ")
guess_word = guess_word.lower()
if guess_word == word:
    print ("Congrats you cracked the code")
elif guess_word != word:
    print ("You failed! Try again.")
