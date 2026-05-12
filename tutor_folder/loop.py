#for loops
#for i in range(5):
    #print("Number:", i)


#while loops
count = int(input("Enter a number: "))
while count <= 100:
    print("Count:", count)
    count += 1


from function import greet
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(greet(name))