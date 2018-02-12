filename = input("Enter file name (without extension): ")
file1 = filename+".txt"
file2 = filename+"_censored.txt"

word = input("Enter the word you are searching for: ")
#In this case, the input would be "winter"

print("\nLooping through the file, line by line.")

in_text_file = open(file1, "r")

out_text_file = open(file2,"w")

8for line in in_text_file:
    print(line)
out_text_file.write(line)

n = [ ]

def censor(word, filename):
    for i in text.split(''):
        if i == word:
            i = "*" * len(word)
            n.append(i)
        else:
            n.append(i)
            return ' '.join(n)
            
in_text_file.close()
out_text_file.close()
