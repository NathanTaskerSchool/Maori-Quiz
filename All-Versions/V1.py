def quiz_choice():
    print("""Learn the following options in Maori:
1. Numbers
2. Days
3. Months""")
    while True:
        user_input = input("What would you like to learn? Input 1-3: ")
        if user_input == "1" or user_input == "2" or user_input == "3":
            break
        else:
            print("Invalid Input. Please try again.")
    return user_input


choice = quiz_choice()
print(choice)
