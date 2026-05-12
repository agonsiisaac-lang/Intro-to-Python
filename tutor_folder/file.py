#with open ("Isaac.txt", "w") as file:
    #file.write("Hello, this is a sample text file.")

with open ("Isaac.txt", "r") as file:
    content = file.read()
    #print(content)

with open ("Isaac.txt", "a") as file:
    file.write("\nThis is an additional line added to the file.")

with open ("Isaac.txt", "r") as file:
    content = file.read()
    print(content)