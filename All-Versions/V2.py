import random
MAORI_NUMBERS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
ENGLISH_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
MAORI_DAYS = ["ratapu", "rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi"]
ENGLISH_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
MAORI_MONTHS = ["kohi-tatea", "hui-tanguru", "poutu-te-rangi", "paenga-whawha", "haratua", "pipiri"]
ENGLISH_MONTHS = ["january", "february", "march", "april", "may", "june"]


def numbers_quiz():
    print("test")


def days_quiz():
    print("test")


def months_quiz():
    print("test")


def get_questions_amount():
    


def get_quiz(user_input):
    if user_input == "1":
        numbers_quiz()
    elif user_input == "2":
        days_quiz()
    elif user_input == "3":
        months_quiz()


def get_quiz_choice():
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


choice = get_quiz_choice()
get_quiz(choice)
