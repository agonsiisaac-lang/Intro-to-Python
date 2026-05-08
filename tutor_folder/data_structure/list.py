food_items = ["apple", "banana", "carrot", "donut"]
print(food_items[0])  # Output: apple
print(food_items[1])  # Output: banana  
print(food_items[2])  # Output: carrot
print(food_items[3])  # Output: donut

# Modifying an element in the list
food_items[1] = "blueberry"
print(food_items[1])  # Output: blueberry

food_items.append("eggplant")
print(food_items)  # Output: ['apple', 'blueberry', 'carrot', 'donut', 'eggplant']

food_items.remove("carrot")
print(food_items)  # Output: ['apple', 'blueberry', 'donut', 'eggplant']