import copy
import datetime
import json
import random
import time

POSSIBLE_ANSWERS = {0: 'a.',1: 'b.', 2: 'c.', 3: 'd.'}
def change_highscore(player_id: str, score: int, path: str = "users.json"):
    try:
        with open(path, "r+") as f:
            players = json.loads(f.read())
            players[player_id]['high_score'] = score
            players[player_id]['date'] = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M")
            f.seek(0)
            f.write(json.dumps(players, indent=4))
    except Exception as e:
        print(f"Failed to save the highscore of {player_id}. \n Error is {e}")
    else:
        print("Successfully saved the new hogh score")


def read_questions(questions_path: str = "questions.json") -> list:
    try:
        with open(questions_path, "r") as f:
            questions = json.loads(f.read())
            questions = questions['questions']
        return questions
    except Exception as e:
        print(f"Fatal error on reading quiz questions : {e}")
        exit(1)

def run_game(player: dict, questions_path: str = "questions.json") -> int:
    scor = 0
    questions = read_questions(questions_path)


    copy_questions = copy.deepcopy(questions)

    while copy_questions:
        questions_obj = random.choice(copy_questions)


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
        change_highscore(player_id=list(player.keys())[0], score=scor)

    return 1

