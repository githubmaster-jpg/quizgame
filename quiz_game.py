level_1 = [
    ["What is 1+1?", "2", "TWO"],
    ["How many colors does a rainbow have?", "7", "SEVEN"],
    ["How many meters are in a kilometer?", "1000", "THOUSAND"],
    ["Which is the smallest month of the year?", "FEBRUARY", "FEBRUARY"],
    ["What animal is known as the king of the jungle?", "LION", "LION"],
]
level_2 = [
    {
        "question": "What is the only letter that doesn’t appear in any U.S. state name?",
        "answer": "The letter 'Q' is the only letter not found in any U.S. state name.",
    },
    {
        "question": "What is the shortest war in history?",
        "answer": "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    },
    {
        "question": "How many hearts does an octopus have?",
        "answer": "An octopus has three hearts: two pump blood to the gills, while the third pumps it to the rest of the body.",
    },
    {
        "question": "What’s the world’s longest place name?",
        "answer": "The longest place name in the world is Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu, a hill in New Zealand.",
    },
    {
        "question": "Which animal can sleep for up to three years?",
        "answer": "Snails can hibernate and sleep for up to three years if the weather conditions aren’t favorable.",
    },
]


def present_question(level, number):
    """Asks the user a question from the level selected. Currently supports one level selection.

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

    Turns the user's answer to capital letters to match the answer list. Try block prevents any errors from stopping the code.
    Answer gets compared to both numerical and text based answer in case the answer should support both. As long as one of the
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
