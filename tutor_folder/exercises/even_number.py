n = int(input("Enter a number: "))

evens = []

for i in range(2, n + 1, 2):
    print(i)
    evens.append(i)

print("Even numbers:", evens)