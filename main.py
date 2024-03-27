# create a quiz game with admin and players. A user has to login.
#if player, then he can play, if admin can add questions
import time
import coloredlogs
import admin_functions
import users
import game


if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")


    curent_player = users.login()

    while True:
        if list(curent_player.keys())[0] == 'admin':
            admin_functions.run()
        else:
            print(f"let's play ")
            game.run_game(curent_player)

            user_pick = input("Do you want to play again? Y/N")
            if user_pick.lower() == 'n':
                break
        time.sleep(2)