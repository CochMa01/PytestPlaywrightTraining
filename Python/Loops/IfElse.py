# Define the age and registration status values
# age = 20
# is_registered = True

# Ask the user to input age and is_registered status
age = int(input("Enter the age: "))
is_registered = input("Is the person registered to vote? (yes/no): ").strip().lower() == 'yes'

# Use an if-elif-else statement to check the conditions
# if age >= 18 and is_registered:
#     print("The person is eligible to vote.")
# elif age >= 18 and not is_registered:
#     print("The person is eligible to vote but not registered.")
# elif 13 <= age <= 17:
#     print("The person is a teenager.")
# elif age >= 65:
#     print("The person is a senior citizen.")
# else:
#     print("The person is not eligible to vote.")

if age >= 18:
    if is_registered:
        print("The person is eligible to vote.")
    else:
        print("The person is eligible to vote but not registered.")
elif 13 <= age <= 17:
    print("The person is a teenager.")
elif age >= 65:
    print("The person is a senior citizen.")
else:
    print("The person is not eligible to vote.")