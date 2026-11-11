


def is_it_on_range(input):
    if int(input) > 9 or int(input) < 1:
        return False
    return True
    
def is_it_a_number(input):
    return input.isdigit()

counter = 1

def play_now():
    if counter % 2 == 0:
        return "o"
    return "x"

def next_turn():
    global counter
    counter += 1

WINNING_LINES = [
(0, 1, 2),
(3, 4, 5),
(6, 7, 8),
(0, 3, 6),
(1, 4, 7),
(2, 5, 8),
(0, 4, 8),
(2, 4, 6),
]

def check_if_we_have_winer():
    if check_if_x_player_win() == True:
        return True
    if check_if_o_player_win() == True:
        return True
    return False


def check_if_x_player_win():
    from functions.box import x_box
    global WINNING_LINES
    x_box = tuple(sorted(x_box))
    for win in WINNING_LINES:
        if all(item in x_box for item in win):
            return True
        else:
            return False

def check_if_o_player_win():
    from functions.box import o_box
    o_box = tuple(sorted(o_box))
    for win in WINNING_LINES:
        if all(item in o_box for item in win):
            return True
    else:
        return False
