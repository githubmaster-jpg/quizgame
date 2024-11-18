import re

level_1 = [
    ["What is 1+1?", "2", "TWO"],
    ["How many colors does a rainbow have?", "7", "SEVEN"],
    ["How many meters are in a kilometer?", "1000", "THOUSAND"],
    ["Which is the smallest month of the year?", "FEBRUARY"],
    ["What animal is known as the king of the jungle?", "LION"],
    [
        "What are the three primary colors of light?",
        "REDGREENBLUE",
        "REDBLUEGREEN",
        "BLUEREDGREEN",
        "BLUEGREENRED",
        "GREENREDBLUE",
        "GREENBLUERED",
    ],
]

level_2 = [["What is 3*5", "15", "FIFTEEN"]]

level_3 = [["What is the capital of Albania?", "TIRANA"]]


def display_levels(levels):
    """
        get list of levels
        then prints a list of available levels.
    Args:
        levels (_type_):
    returns:
        nothing.
    """
    for i, level in enumerate(levels):
        print(f"{i + 1 }. {level}")


def get_level(levels):
    """
    ask the user to pick the level
    user picks a number

    returns:
        selected level -> str
    """
    while True:
        try:
            choice = int(input("Select level ")) - 1
            for i in range(len(levels)):
                if levels[choice] == levels[i]:
                    print(f"you have selected {levels[choice].replace('_', ' ')}")
                    return levels[i]

        except (ValueError, IndexError):
            pass


def present_question(level: list, number: int) -> str:
    """Asks the user a question from the level selected.

    Parameters
    ----------
    level : list
        The container listing questions and answers
    number : int
        Number of question

    Returns
    -------
    answer : str
        User's answer to the given question
    """

    answer = input(f"Question {number}: {level[number-1][0]}: ")
    return answer


def check_answer(level, answer, number, correct):
    """Checks the user's answer and compares it to the correct one. Currently supports one level selection.

    Turns the user's answer to capital letters to match the answer list. Removes 'and' and other special characters from answer.
    Try block prevents any errors from stopping the code. Answer gets compared to the answers in list. As long as one of the
    correct answers is detected, the answer will be marked as correct. If a wrong or an error causing answer is submitted by
    the user, the answer will be marked incorrect.

    Parameters
    ----------
    level : list
        The container listing questions and answers
    answer : str
        User's answer to the given question
    number : int
        Number of question
    correct : int
        Number of correct answers, starting from 0

    Returns
    -------
    int
        Returns 1 if the answer is correct, 0 if the answer is incorrect
    """

    answer = answer.upper()
    answer = answer.replace(" AND ", "")
    answer = re.sub(r"[^a-zA-Z0-9]", "", answer)
    try:
        if answer == level[number - 1][1] or answer == level[number - 1][2]:
            print(f"Good job!\nCorrect amount of answers: {correct+1}")
            return 1
        else:
            print("Wrong answer")
            return 0
    except:
        print("Wrong answer")
        return 0


def main():
    """Enables the quiz game to run.

    The 'correct' and 'number' variables increase as the game progresses. There is no way to decrease
    them by the time of this update. The 'questions' takes the len of the list, allowing it to run
    through all the questions in a level container. While loop is used to one by one present questions
    and check for the correct answers. The amount of correct answers gets printed to the user at the
    end of the game.
    """
    levels = levels = ["level_1", "level_2", "level_3"]
    display_levels(levels)
    level = get_level(levels)
    print(level)
    correct = 0
    number = 1
    questions = len(level_1)
    while number <= questions:
        answer = present_question(level_1, number)
        correct_answer = check_answer(level_1, answer, number, correct)
        correct = correct + correct_answer
        number += 1
    print(f"Total amount of correct answers: {correct}")


if __name__ == "__main__":
    main()
