kbinput = str(input("Enter Text: "))
sentence = ""
sentence = kbinput.lower()
vowels = "aeiou"
revsentence = ""
for ch in vowels:
	sentence=sentence.replace(ch, ch.upper())
revsentence=sentence[::-1]
print (sentence)
print (revsentence)
