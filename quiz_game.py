import re
from termcolor import colored

level_1 = [['What is 1+1?', '2', 'TWO'],
          ['How many colors does a rainbow have?', '7', 'SEVEN'],
          ['How many meters are in a kilometer?', '1000', 'THOUSAND'],
          ['Which is the smallest month of the year?', 'FEBRUARY'],
          ['How many legs does a spider have?', '8', 'EIGHT']
          ]

level_2 = [['What is 3*10-6*5?', '0', 'ZERO'],
          ['What is the capital of Albania?', 'TIRANA'],
          ['What type of chemical elements is water composed of?', 'HYDROGENOXYGEN', 'OXYGENHYDROGEN', 'OH', 'HO'],
          ['What is the name of the second tallest mountain?', 'K2'],
          ['Who is the painter of "The Starry Night"?', 'VINCENTVANGOGH', 'VANGOGH', 'VANGOGHVINCENT']
           ]

level_3 = [['What animal is known as the king of the jungle?', 'LION'],
          ['What are the three primary colors of light?', 'REDGREENBLUE', 'REDBLUEGREEN', 'BLUEREDGREEN', 'BLUEGREENRED', 'GREENREDBLUE','GREENBLUERED'],
          ["What is Scotland's national animal?", 'UNICORN'],
          ['What is at the end of the rainbow?', 'W', 'POTOFGOLD', 'APOTOFGOLD', 'GOLD'],
          ['What is x in "(x-3)(x+5)=9"?', '46','64']
           ]

levels = [level_1, level_2, level_3]


def present_question(level:list, number:int) -> str:
    """ Asks the user a question from the level selected.

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

    answer = input(colored(f'\nQuestion {number}: {level[number-1][0]}: ', 'light_yellow'))
    return answer


def check_answer(level:list, answer:str, number:int, lives:int) -> int:
    """ Checks the user's answer and compares it to the correct one.

    Turns the user's answer to capital letters to match the answer list. Removes 'and', 'or' and other special characters 
    from answer. Try block prevents any errors from stopping the code. Answer gets compared to the answers in list. 
    As long as one of the correct answers is detected, the answer will be marked as correct. If a wrong or an error causing
    answer is submitted by the user, the answer will be marked incorrect and they will lose a life.

    Parameters
    ----------
    level : list
        The container listing questions and answers
    answer : str
        User's answer to the given question
    number : int
        Number of question
    lives : int
        Number of lives
    
    Returns
    -------
    int
        Returns 1 if the answer is correct, -1 if the answer is incorrect
    """
    
    answer = answer.upper()
    answer = answer.replace(' AND ', '')
    answer = answer.replace(' OR ', '')
    answer = re.sub(r'[^a-zA-Z0-9]','',answer)
    try:
        if answer in level[number-1]:
            print(colored(f'\nCorrect answer, good job!', 'green'))
            return 1
        else:
            if lives-1 == 1:
                print(colored(f'\nWrong answer, {lives-1} life remaining!', 'red'))
            else:    
                print(colored(f'\nWrong answer, {lives-1} lives remaining!', 'red'))
            return -1
    except:
        print(colored(f'\nWrong answer, {lives-1} lives remaining!', 'red'))
        return -1


def total_correct(levels:list, all_correct:int) -> None:
    """Prints a line depending on the amount of correct answers
    
    Checks the total amount of question answers from the question lists. Divides the
    player's score with the total amount of questions for a grading, and prints a line
    depending on the grade. Returns nothing.

        Parameters
    ----------
    levels : list
        The container with all quiz level lists
    all_correct : int
        User's total amount of correct answers
    
    Returns
    -------
    None
    """

    answers_total = 0
    for list in levels:
        answers_total += len(list)
    if all_correct == answers_total:
        print(colored(f'\nTotal amount of points: {all_correct}/{answers_total}!\n\nAmazing! You answered everything correctly!', 'green'))
    elif all_correct/answers_total >= 0.75:
        print(colored(f'\nTotal amount of points: {all_correct}/{answers_total}!\n\nGreat job! You almost got all correct!', 'blue'))
    elif all_correct/answers_total >= 0.50:
        print(colored(f'\nTotal amount of points: {all_correct}/{answers_total}!\n\nGood job, you got at least half correct!', 'light_blue'))
    elif all_correct/answers_total >= 0.25:
        print(colored(f'\nTotal amount of points: {all_correct}/{answers_total}.\n\nGood effort, but perhaps you can get a few more correct?', 'light_magenta'))
    else:
        print(colored(f'\nTotal amount of points: {all_correct}/{answers_total}!\n\nToo bad, maybe you will do better next try?','magenta'))
    return None


def main():
    """ Enables the quiz game to run.
    """
    print(colored("\nWelcome to the quiz game!\n\nGame rules:\n\n1. Try to answer correctly!\n2. If you don't answer correctly, don't worry!\n   You get 3 lives per level.\n3. Don't get too careless though, because if you\n   run out of lives on a level the whole game will end!\n4. Have fun!\n\nLet's get started!",'light_cyan'))
    game_round = 0
    all_levels = len(levels)
    all_correct = 0  
    live_checker = 0
    while game_round+1 <= all_levels and live_checker == 0:
        correct = 0
        lives = 3
        number = 1
        questions = len(levels[game_round])
        print(colored(f'\nQuiz Level {game_round+1}:', 'light_blue'))
        while number <= questions:
            if lives == 0:
                print(colored('\nNo more lives remaining.', 'red'))
                live_checker = live_checker-1
                break
            else:
                answer=present_question(levels[game_round], number)
                correct_answer = check_answer(levels[game_round],answer,number,lives)
                if correct_answer < 0:
                    lives = lives + correct_answer
                else:
                    correct = correct + correct_answer
            number += 1
        print(colored(f'\nLevel {game_round+1} finished!', 'light_blue'))
        all_correct = all_correct + correct
        game_round += 1
    total_correct(levels,all_correct)
    

if __name__ == "__main__":
    main()
