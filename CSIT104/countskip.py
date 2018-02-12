print("Welcome! I can make counting easier for you.")

start_num = int(input("Please give me a starting number. "))
end_num = int(input("Please give me an ending number. "))
interval = int(input("By which amount am I to count? "))

print ("Counting:")
for i in range(start_num, end_num, interval):
    print (i)
