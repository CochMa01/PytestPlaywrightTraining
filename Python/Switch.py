def day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

if __name__ == "__main__":
    day = input("Enter a day of the week: ")
    print(day_type(day))
