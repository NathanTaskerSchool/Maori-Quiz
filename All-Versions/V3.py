import random

MAORI_NUMBERS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
ENGLISH_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
MAORI_DAYS = ["ratapu", "rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi"]
ENGLISH_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
MAORI_MONTHS = ["kohi-tatea", "hui-tanguru", "poutu-te-rangi", "paenga-whawha", "haratua", "pipiri"]
ENGLISH_MONTHS = ["january", "february", "march", "april", "may", "june"]


def ask_question(quiz_type):
    print("question asked")


def run_quiz(quiz_type, total_questions):
    questions_left = total_questions
    while questions_left > 0:
        ask_question(quiz_type)
        questions_left -= 1


def get_total_questions():
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


def get_quiz_type():
    print("""Learn the following options in Maori:
1. Numbers
2. Days
3. Months""")
    while True:
        user_input = input("What would you like to learn? Input 1-3: ")
        if user_input == "1" or user_input == "2" or user_input == "3":
            return user_input
        else:
            print("Invalid Input. Please try again.")


def ask_to_play_again():
    while True:
        user_input = input("Would you like to play another quiz? Input y/n: ")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        print("Invalid input. Please try again.")


while True:
    run_quiz(get_quiz_type(), get_total_questions())
    if not ask_to_play_again():
        break
