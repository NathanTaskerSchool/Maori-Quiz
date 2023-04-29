import random

MAORI_NUMBERS = ["kore", "tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
ENGLISH_NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
MAORI_DAYS = ["ratapu", "rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi"]
ENGLISH_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
MAORI_MONTHS = ["kohi-tatea", "hui-tanguru", "poutu-te-rangi", "paenga-whawha", "haratua", "pipiri",
                "hongongoi", "here-turi-koka", "mahuru", "whiringa-a-nuku", "whiringa-a-rangi", "hakihea"]
ENGLISH_MONTHS = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november", "december"]


def number_question():
    random_index = random.randint(0, 10)
    if random.randint(0, 1) == 0:
        # Maori Input
        user_input = input(f'Input the Maori word for "{ENGLISH_NUMBERS[random_index]}": ')
        if user_input.lower().strip() == MAORI_NUMBERS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The Maori word for {ENGLISH_NUMBERS[random_index]} is {MAORI_NUMBERS[random_index]}.")
            return 0
    else:
        # English or number input
        user_input = input(f'Input the number or English word for "{MAORI_NUMBERS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_NUMBERS[random_index]:
            print("Correct!")
            return 1
        elif user_input.strip() == NUMBERS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The English word for {MAORI_NUMBERS[random_index]} is {ENGLISH_NUMBERS[random_index]}.")
            return 0


def day_question():
    random_index = random.randint(0, 6)
    if random.randint(0, 1) == 0:
        # Maori Input
        user_input = input(f'Input the Maori word for "{ENGLISH_DAYS[random_index]}": ')
        if user_input.lower().strip() == MAORI_DAYS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The Maori word for {ENGLISH_DAYS[random_index]} is {MAORI_DAYS[random_index]}.")
            return 0
    else:
        # English Input
        user_input = input(f'Input the English word for "{MAORI_DAYS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_DAYS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The English word for {MAORI_DAYS[random_index]} is {ENGLISH_DAYS[random_index]}.")
            return 0


def month_question():
    random_index = random.randint(0, 11)
    if random.randint(0, 1) == 0:
        # Maori Input
        user_input = input(f'Input the Maori word for "{ENGLISH_MONTHS[random_index]}": ')
        if user_input.lower().strip() == MAORI_MONTHS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The Maori word for {ENGLISH_MONTHS[random_index]} is {MAORI_MONTHS[random_index]}.")
            return 0
    else:
        # English Input
        user_input = input(f'Input the English word for "{MAORI_MONTHS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_MONTHS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The English word for {MAORI_MONTHS[random_index]} is {ENGLISH_MONTHS[random_index]}.")
            return 0


def ask_question(quiz_type):
    if quiz_type == "1":
        return number_question()
    elif quiz_type == "2":
        return day_question()
    elif quiz_type == "3":
        return month_question()


def run_quiz(quiz_type, total_questions):
    questions_left = total_questions
    score = 0
    while questions_left > 0:
        print(f"\n- QUESTION #{total_questions - questions_left + 1}")
        score += ask_question(quiz_type)
        questions_left -= 1
    print(f"\nEnd of quiz. You scored {score}/{total_questions}.")


def get_total_questions():
    while True:
        try:
            user_input = int(input("How many questions would you like? Input a number: ").strip())
            if user_input < 1:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    return user_input


def get_quiz_type():
    print("""\nLearn the following options in Maori:
1. Numbers
2. Days
3. Months""")
    while True:
        user_input = input("What would you like to learn? Input 1-3: ").strip()
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
