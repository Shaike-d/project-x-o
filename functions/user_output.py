import functions.validation as v
import functions.box as b


def user_chooce():
    while True:
        b.print_board_game()
        print(f"now is turn {v.play_now()} to play")
        choice = input("Please enter the number of the square you wish to mark ")
        if choice == "":
            print("con't be empty")
            continue
        if v.is_it_on_range(choice) == True:
            if v.is_it_a_number(choice) == True:
                return int(choice)
            else:
                print("You must enter a whole number ")
                continue
        else:
            print("the number out of range")
            continue

