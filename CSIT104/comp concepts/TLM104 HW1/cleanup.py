kbinput = str(input("input string to be modified"))

kbfinal = ""
vowels = "aeiou"
bs = "bv"

for ch in vowels:
	kbinput=kbinput.replace(ch, "")
for x in range (0,len(kbinput)):
	if kbinput[x]=="b":
		kbfinal+="v"
	elif kbinput[x]=="v":
		kbfinal+="b"
	else:
		kbfinal+=kbinput[x]	
print (kbfinal)
