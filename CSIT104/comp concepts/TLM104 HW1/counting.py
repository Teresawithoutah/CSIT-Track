kbinput = str(input("Enter Text: "))
charnum = 0
wordcount = 0
for ch in kbinput:
	if ch == " ":
		wordcount+= 1
	else:
		charnum += 1
print ("the amount of words")
print (wordcount+1)
print ("the amount of characters")
print (charnum+1)
