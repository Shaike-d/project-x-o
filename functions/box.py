board_game = [[['1'],['2'],['3']],
              [['4'],['5'],['6']],
              [['7'],['8'],['9']]
              ]

def print_board_game():
    for row in board_game:
        for item in row:
            print(item, end=' ')
        print()
        
def is_the_box_free(boxnum):
    location = box_in_board_game(boxnum)
    if location == ['x'] or location == ['o']:
        return False
    return True
        


def change_box(boxnum,player):
    location = box_in_board_game(boxnum)
    location.pop(0)
    location.append(player)


def box_in_board_game(input):
    if int(input) == 1:
        return board_game[0][0]
    if int(input) == 2:
        return board_game[0][1]
    if int(input) == 3:
        return board_game[0][2] 
    if int(input) == 4:
        return board_game[1][0]
    if int(input) == 5:
        return board_game[1][1] 
    if int(input) == 6:
        return board_game[1][2]
    if int(input) == 7:
        return board_game[2][0]
    if int(input) == 8:
        return board_game[2][1]
    if int(input) == 9:
        return board_game[2][2]
        
x_box = []
o_box = []

def add_box_to_player(player,boxnum):
    global x_box,o_box
    if player == "x":
        x_box.append(int(boxnum)-1)
    if player == "o":
        o_box.append(int(boxnum)-1)



