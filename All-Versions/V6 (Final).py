import random

MAORI_NUMBERS = ["kore", "tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                 "waru", "iwa", "tekau"]
ENGLISH_NUMBERS = ["zero", "one", "two", "three", "four", "five", "six",
                   "seven", "eight", "nine", "ten"]
NUMBERS = [str(i) for i in range(11)]
MAORI_DAYS = ["ratapu", "rahina", "ratu", "raapa", "rapare", "ramere",
              "rahoroi"]
ENGLISH_DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday",
                "friday", "saturday"]
MAORI_MONTHS = ["kohi-tatea", "hui-tanguru", "poutu-te-rangi", "paenga-whawha",
                "haratua", "pipiri", "hongongoi", "here-turi-koka", "mahuru",
                "whiringa-a-nuku", "whiringa-a-rangi", "hakihea"]
ENGLISH_MONTHS = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november",
                  "december"]
NUMBERS_QUIZ_INDEX = 1
DAYS_QUIZ_INDEX = 2
MONTHS_QUIZ_INDEX = 3


# Asks the user a randomly generated number question, returning a score value
def number_question():
    random_index = random.randint(0, 10)
    if random.randint(0, 1) == 0:
        # 50% chance that the user must input a Maori word
        user_input = input(f'Input the Maori word for'
                           f' "{ENGLISH_NUMBERS[random_index]}": ')
        if user_input.lower().strip() == MAORI_NUMBERS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The Maori word for'
                  f' "{ENGLISH_NUMBERS[random_index]}" is '
                  f'"{MAORI_NUMBERS[random_index]}".')
            return 0
    else:
        # 50% chance that the user must input a number or English word
        user_input = input(f'Input the number or English word for'
                           f' "{MAORI_NUMBERS[random_index]}": ')
        if user_input.lower().strip() in [ENGLISH_NUMBERS[random_index],
                                          NUMBERS[random_index]]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The English word for'
                  f' "{MAORI_NUMBERS[random_index]}" is '
                  f'"{ENGLISH_NUMBERS[random_index]}".')
            return 0


# Asks the user a randomly generated day question, returning a score value
def day_question():
    random_index = random.randint(0, 6)
    if random.randint(0, 1) == 0:
        # 50% chance that the user must input a Maori word
        user_input = input(f'Input the Maori word for'
                           f' "{ENGLISH_DAYS[random_index]}": ')
        if user_input.lower().strip() == MAORI_DAYS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The Maori word for'
                  f' "{ENGLISH_DAYS[random_index]}" is'
                  f' "{MAORI_DAYS[random_index]}".')
            return 0
    else:
        # 50% chance that the user must input an English word
        user_input = input(f'Input the English word for'
                           f' "{MAORI_DAYS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_DAYS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The English word for'
                  f' "{MAORI_DAYS[random_index]}" is'
                  f' "{ENGLISH_DAYS[random_index]}".')
            return 0


# Asks the user a randomly generated month question, returning a score value
def month_question():
    random_index = random.randint(0, 11)
    if random.randint(0, 1) == 0:
        # 50% chance that the user must input a Maori word
        user_input = input(f'Input the Maori word for'
                           f' "{ENGLISH_MONTHS[random_index]}": ')
        if user_input.lower().strip() == MAORI_MONTHS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The Maori word for'
                  f' "{ENGLISH_MONTHS[random_index]}" is'
                  f' "{MAORI_MONTHS[random_index]}".')
            return 0
    else:
        # 50% chance that the user must input an English word
        user_input = input(f'Input the English word for'
                           f' "{MAORI_MONTHS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_MONTHS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The English word for'
                  f' "{MAORI_MONTHS[random_index]}" is '
                  f'"{ENGLISH_MONTHS[random_index]}".')
            return 0


# Calls the correct function depending on the given parameter (quiz_index)
def ask_question(quiz_index):
    if quiz_index == NUMBERS_QUIZ_INDEX:
        return number_question()
    elif quiz_index == DAYS_QUIZ_INDEX:
        return day_question()
    elif quiz_index == MONTHS_QUIZ_INDEX:
        return month_question()


# Asks a new question as long as it hasn't reached the value previously input
# as questions wanted by the user
def run_quiz(quiz_type, total_questions):
    questions_asked = 0
    score = 0
    while questions_asked < total_questions:
        print(f"\nQUESTION {questions_asked + 1}")
        score += ask_question(quiz_type)
        questions_asked += 1
    print(f"\nEnd of quiz. You scored {score}/{total_questions}.")


# Asks the user how many questions they would like to be quizzed on, and
# accepts the input if it is a positive integer
def get_total_questions():
    while True:
        try:
            user_input = int(input("How many questions would you like? Input a"
                                   " number: ").strip())
            if user_input < 1:
                print("Please enter a positive integer.")
            else:
                return user_input
        except ValueError:
            print("Please enter a valid integer.")


# This function displays the quiz types available and asks the user what they
# want to learn, returning if input is valid
def get_quiz_type():
    print(f"""\nLearn the following options in Maori:
{NUMBERS_QUIZ_INDEX}. NUMBERS
{DAYS_QUIZ_INDEX}. DAYS
{MONTHS_QUIZ_INDEX}. MONTHS""")
    while True:
        user_input = input("What would you like to learn? Input 1-3: ").strip()
        if user_input in str([NUMBERS_QUIZ_INDEX, DAYS_QUIZ_INDEX,
                              MONTHS_QUIZ_INDEX]):
            return int(user_input)
        else:
            print("Invalid Input. Please try again.")


# This function simply asks the user if they want to play again, returning
# either true or false depending on their input
def ask_to_play_again():
    while True:
        user_input = input("Would you like to play another quiz?"
                           " Input y/n: ").lower().strip()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        print("Invalid input. Please try again.")


# This function is an infinite loop that will only break and end the program
# once the user decides to no longer play
def start():
    while True:
        run_quiz(get_quiz_type(), get_total_questions())
        if not ask_to_play_again():
            break


start()
