import json


def add_user(player_id: str, all_players: dict, path: str = "users.json") -> dict:

    full_name = input("Introdu numele tau: ")
    full_name = player_id if full_name == "" or not full_name.isalnum() else full_name
    password = ""
    confirm_pass = " "
    while len(password) < 3:
        while password != confirm_pass:
            password = input("Introdu parola: ")
            confirm_pass = input("Confirma parola: ")
            if len(password) < 3:
                password = ""
                confirm_pass = " "
                print("Parola este prea mica")

    new_user = {player_id: {"full_name": full_name, "high_score": 0, "password": password}}
    all_players.update(new_user)
    with open(path, "w") as f:
        f.write(json.dumps(all_players, indent=4))

    return new_user



def login(path: str = "users.json"):
    is_new_user = False
    new_user = {}
    user = input("Log in: ")

    with open(path, "r") as f:
        users = json.loads(f.read())

    if user not in users:
        user_pick = input("Doresti sa te inscrii ca nou jucator? Y/N ")
        if user_pick.lower() == "y":
            new_user = add_user(player_id=user, all_players=users)
            is_new_user = True
        else:
            while user not in users:
                user = input("Log in, utilizatorul nu exista: ")
    if not is_new_user:
        password = input("Adauga o parola: ")
        counter = 0
        while password != users[user]['password']:
            password = input("Parola gresita. Reintrodu parola: ")
            counter += 1
            if counter == 3:
                raise Exception("Parola a fost introdusa de prea multe ori")
    else:
        return new_user

    return {user: users[user]}
