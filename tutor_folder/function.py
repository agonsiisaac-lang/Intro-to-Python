"""Parts of a function
1. def - this is the keyword that tells Python we are defining a function
2. greet - this is the name of the function, you can choose any name you like
3. (name) - this is the parameter of the function, it is a variable that will hold the value that we pass to the function when we call it
4. : - this is the colon that indicates the start of the function body
5. return - this is the keyword that tells Python to return a value from the function
6. "Hello," + name - this is the value that we are returning from the function, it is a string that concatenates "Hello," with the value of the parameter name
7. print(greet("Isaac")) - this is how we call the function, we pass the value "Isaac" to the parameter name and print the result
"""

def greet(name = "zion"):
    return "Hello," + name
#print(greet("Isaac"))


def area_of_rectangle(length, width=2):
    return length * width
#print(area_of_rectangle(5,3))


