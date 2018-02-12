filename = input("Enter file name (without extension): ")
fil1 = filename+".txt"
fil2 = filename+"_censored.txt"

word = input("Enter Word you are looking for: ")

print("\nLooping through the file, line by line.")


fil2.write(fil1.read().replace(word, "*"*len(word)))
fil1.close()
fil2.close()