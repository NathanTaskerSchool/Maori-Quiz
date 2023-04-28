import random

MAORI_NUMBERS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
ENGLISH_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
MAORI_DAYS = ["ratapu", "rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi"]
ENGLISH_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
MAORI_MONTHS = ["kohi-tatea", "hui-tanguru", "poutu-te-rangi", "paenga-whawha", "haratua", "pipiri"]
ENGLISH_MONTHS = ["january", "february", "march", "april", "may", "june"]


def run_quiz(total_questions, quiz_type):
    questions_left = total_questions
    while questions_left > 0:
        ask_numbers_question()
        questions_left -= 1


def get_questions_amount():
    while True:
        try:
            user_input = int(input("How many question would you like? Input a number: "))
            if user_input < 1:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    return user_input


def get_quiz(user_input):
    if user_input == "1":
        run_quiz(get_questions_amount(), 1)
    elif user_input == "2":
        run_quiz(get_questions_amount(), 1)
    elif user_input == "3":
        run_quiz(get_questions_amount(), 1)


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
