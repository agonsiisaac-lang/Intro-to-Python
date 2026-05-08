#nested conditions

"""Key Concepts:
• Use "and", "or", "not" for combining multiple conditions
• Nested if/else allows multiple decision paths
• "and" requires both conditions to be true
• "or" requires at least one condition to be true
• "not" reverses the boolean value"""

score = int(input("Enter your score: "))

if score >= 70 and score <= 100:
    print("Print Grade: A")
elif score >= 50 and score < 70:
    print("Print Grade: B")
elif score >= 101:
    print("Invalid score")
else:
    print("Failed")
