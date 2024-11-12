import re
level_1 = [['What is 1+1?', '2', 'TWO'],
          ['How many colors does a rainbow have?', '7', 'SEVEN'],
          ['How many meters are in a kilometer?', '1000', 'THOUSAND'],
          ['Which is the smallest month of the year?', 'FEBRUARY'],
          ['What animal is known as the king of the jungle?', 'LION'],
          ['What are the three primary colors of light?', 'REDGREENBLUE', 'REDBLUEGREEN', 'BLUEREDGREEN', 'BLUEGREENRED', 'GREENREDBLUE','GREENBLUERED']
          ]

level_2 = [['What is 3*5', '15', 'FIFTEEN']
           ]

level_3 = [['What is the capital of Albania?', 'TIRANA']
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

    answer = input(f'Question {number}: {level[number-1][0]}: ')
    return answer


def check_answer(level:list, answer:str, number:int, correct:int) -> int:
    """ Checks the user's answer and compares it to the correct one.

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
    answer = answer.replace(' AND ', '')
    answer = re.sub(r'[^a-zA-Z0-9]','',answer)
    try:
        if answer in level[number-1]:
            print(f'Good job!\nCorrect amount of answers: {correct+1}')
            return 1
        else:
            print('Wrong answer')
            return 0
    except:
        print('Wrong answer')
        return 0


def main():
    """ Enables the quiz game to run.
    """
    
    game_round = 0
    all_levels = len(levels)
    all_correct = 0  
    while game_round+1 <= all_levels:
        correct = 0
        number = 1
        questions = len(levels[game_round])
        print(f'Quiz Level {game_round+1}:')
        while number <= questions:
            answer=present_question(levels[game_round], number)
            correct_answer = check_answer(levels[game_round],answer,number,correct)
            correct = correct + correct_answer
            number += 1
        #print(f'Amount of correct answers in level: {correct}') # prints number of correct answers after finishing a level, but the check function prints it after every correct answer at this moment
        all_correct = all_correct + correct
        game_round += 1
    print(f'Total amount of correct answers: {all_correct}')
    

if __name__ == "__main__":
    main()
