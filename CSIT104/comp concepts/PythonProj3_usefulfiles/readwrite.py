# Stefan Robila
# readwrite.py
# Demonstrates reading from a text file and writing to the other

filename = input("Enter file name (without extension): ")
fil1 = filename+".txt"
fil2 = filename+"_censored.txt"


print("\nLooping through the file, line by line.")
in_text_file = open(fil1, "r")
out_text_file = open(fil2,"w")
for line in in_text_file:
    print(line)
    out_text_file.write(line)
in_text_file.close()
out_text_file.close()


