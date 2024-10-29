age = int(input("Please enter your age: "))

is_senior = age >= 60
is_youth = age < 18

print(f"Your age is {age}")
print(f"Eligible for senior citizen discount: {is_senior}")
print(f"Eligible for youth discount: {is_youth}")
