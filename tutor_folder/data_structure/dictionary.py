profile = {
    "name": "Zion",
    "age": 25,
    "city": "Owerri",
    "hobbies": ["coding", "gaming", "traveling"]
}

print("Name:", profile["name"])
print("Age:", profile["age"])   
print("City:", profile["city"])
print("Hobbies:", profile["hobbies"])

# Modifying an element in the dictionary
profile["age"] = 26
print("Age:", profile["age"])   
profile["hobbies"].append("cooking")
print("Hobbies:", profile["hobbies"])   

# Removing an element from the dictionary
del profile["city"]
print("City:", profile.get("city", "Not specified"))