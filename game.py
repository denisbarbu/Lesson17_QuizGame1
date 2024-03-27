import copy
import json
import random
import time

POSSIBLE_ANSWERS = {0: 'a.',1: 'b.', 2: 'c.', 3: 'd.'}
def change_highscore():
    pass
def run_game(player: dict, questions_path: str = "questions.json") -> int:
    scor = 0
    with open(questions_path, "r") as f:
        questions = json.loads(f.read())
        questions = questions['questions']


    copy_questions = copy.deepcopy(questions)

    while copy_questions:
        questions_obj = random.choice(copy_questions)

        print(questions_obj)
        print(questions_obj['question'])
        for index, answer in enumerate(questions_obj['answers']):
            print(f"{POSSIBLE_ANSWERS[index]} {answer}")

        pick = input("Alege raspunsul corect: ")
        answers = {v: k for k, v in POSSIBLE_ANSWERS.items()}
        if answers[f"{pick}."] == questions_obj['correctIndex']:
            print("Coreect answer")
            scor += 1
        else:
            print("Wrong answer")


        copy_questions.remove(questions_obj)
        time.sleep(1)

    print(f"You have answered to {scor} questions")

    if scor > player[list(player.keys())[0]]['high_score']:
        change_highscore()

    return 1

