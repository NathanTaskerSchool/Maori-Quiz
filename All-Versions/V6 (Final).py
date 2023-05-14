import random

MAORI_NUMBERS = ["kore", "tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
ENGLISH_NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
NUMBERS = [str(i) for i in range(11)]
MAORI_DAYS = ["Ratapu", "Rahina", "Ratu", "Raapa", "Rapare", "Ramere", "Rahoroi"]
ENGLISH_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
MAORI_MONTHS = ["Kohi-tatea", "Hui-tanguru", "Poutu-te-rangi", "Paenga-whawha", "Haratua", "Pipiri",
                "Hongongoi", "Here-turi-koka", "Mahuru", "Whiringa-a-nuku", "Whiringa-a-rangi", "Hakihea"]
ENGLISH_MONTHS = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
NUMBERS_QUIZ_INDEX = 1
DAYS_QUIZ_INDEX = 2
MONTHS_QUIZ_INDEX = 3


def number_question():
    random_index = random.randint(0, 10)
    if random.randint(0, 1) == 0:
        # 50% chance that the user must input a Maori word
        user_input = input(f'Input the Maori word for "{ENGLISH_NUMBERS[random_index]}": ')
        if user_input.lower().strip() == MAORI_NUMBERS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The Maori word for "{ENGLISH_NUMBERS[random_index]}" is '
                  f'"{MAORI_NUMBERS[random_index]}".')
            return 0
    else:
        # 50% chance that the user must input a number or English word
        user_input = input(f'Input the number or English word for "{MAORI_NUMBERS[random_index]}": ')
        if user_input.lower().strip() in [ENGLISH_NUMBERS[random_index], NUMBERS[random_index]]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The English word for "{MAORI_NUMBERS[random_index]}" is '
                  f'"{ENGLISH_NUMBERS[random_index]}".')
            return 0


def day_question():
    random_index = random.randint(0, 6)
    if random.randint(0, 1) == 0:
        # 50% chance that the user must input a Maori word
        user_input = input(f'Input the Maori word for "{ENGLISH_DAYS[random_index]}": ')
        if user_input.lower().strip() == MAORI_DAYS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The Maori word for "{ENGLISH_DAYS[random_index]}" is "{MAORI_DAYS[random_index]}".')
            return 0
    else:
        # 50% chance that the user must input an English word
        user_input = input(f'Input the English word for "{MAORI_DAYS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_DAYS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The English word for "{MAORI_DAYS[random_index]}" is "{ENGLISH_DAYS[random_index]}".')
            return 0


def month_question():
    random_index = random.randint(0, 11)
    if random.randint(0, 1) == 0:
        # 50% chance that the user must input a Maori word
        user_input = input(f'Input the Maori word for "{ENGLISH_MONTHS[random_index]}": ')
        if user_input.lower().strip() == MAORI_MONTHS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The Maori word for "{ENGLISH_MONTHS[random_index]}" is "{MAORI_MONTHS[random_index]}".')
            return 0
    else:
        # 50% chance that the user must input an English word
        user_input = input(f'Input the English word for "{MAORI_MONTHS[random_index]}": ')
        if user_input.lower().strip() == ENGLISH_MONTHS[random_index]:
            print("Correct!")
            return 1
        else:
            print(f'Incorrect. The English word for "{MAORI_MONTHS[random_index]}" is '
                  f'"{ENGLISH_MONTHS[random_index]}".')
            return 0


def ask_question(quiz_index):
    if quiz_index == NUMBERS_QUIZ_INDEX:
        return number_question()
    elif quiz_index == DAYS_QUIZ_INDEX:
        return day_question()
    elif quiz_index == MONTHS_QUIZ_INDEX:
        return month_question()


def run_quiz(quiz_type, total_questions):
    questions_left = total_questions
    score = 0
    while questions_left > 0:
        print(f"\nQUESTION {total_questions - questions_left + 1}")
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
    print(f"""\nLearn the following options in Maori:
{NUMBERS_QUIZ_INDEX}. NUMBERS
{DAYS_QUIZ_INDEX}. DAYS
{MONTHS_QUIZ_INDEX}. MONTHS""")
    while True:
        user_input = input("What would you like to learn? Input 1-3: ").strip()
        if user_input in str([NUMBERS_QUIZ_INDEX, DAYS_QUIZ_INDEX, MONTHS_QUIZ_INDEX]):
            return int(user_input)
        else:
            print("Invalid Input. Please try again.")


def ask_to_play_again():
    while True:
        user_input = input("Would you like to play another quiz? Input y/n: ").lower().strip()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        print("Invalid input. Please try again.")


def start():
    while True:
        run_quiz(get_quiz_type(), get_total_questions())
        if not ask_to_play_again():
            break


start()
