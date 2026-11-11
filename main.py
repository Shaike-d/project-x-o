import functions.user_output as u
import functions.validation as v
import functions.box as b
def main():
    while True:
        chooce = u.user_chooce()
        player = v.play_now()
        if b.is_the_box_free(chooce) == False:
            print("the box is alrady in use")
            continue
        else:
            b.change_box(chooce,player)
            b.add_box_to_player(player,chooce)
            if v.check_if_we_have_winer() == True:
                print(f"player {player} is a winner")
                exit()
            v.next_turn()
            
            














if __name__ == "__main__":
    main()
