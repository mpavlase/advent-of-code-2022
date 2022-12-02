# oponent ABC - rock, paper, scissors
# mine XYZ - rock, paper, scissors

# outcome of round
# X - loose
# Y - draw
# Z - win

from enum import Enum


class Choice(Enum):
    rock = 'A'
    paper = 'B'
    scissors = 'C'


class Outcome(Enum):
    loose = 'X'
    draw = 'Y'
    win = 'Z'

first_win_situations = [
    (Choice.rock, Choice.scissors),
    (Choice.paper, Choice.rock),
    (Choice.scissors, Choice.paper)
]



def first_win(first, second):
    return (first, second) in first_win_situations


def is_draw(first, second):
    return first == second


def translate_mine_to_oponent(choice):
    return {
        'X': Choice.rock,
        'Y': Choice.paper,
        'Z': Choice.scissors
    }[choice]


def get_shape_score(shape):
    shape_score = {
        Choice.rock: 1,
        Choice.paper: 2,
        Choice.scissors: 3
    }

    return shape_score[shape]


def get_my_choice(oponent, outcome):
    if outcome == Outcome.draw:
        return oponent

    if outcome == Outcome.win:
        for first, second in first_win_situations:
            if second == oponent:
                return first

        assert False, f'{outcome=}, this should not happend'

    if outcome == Outcome.loose:
        for first, second in first_win_situations:
            if first == oponent:
                return second

        assert False, f'{outcome=}, this should not happend'
    assert False, f'{outcome=}, this should not happend'





total_score = 0


with open('input') as fd:
    for line in fd.readlines():
        line = line.strip()

        turn_first, turn_second = line.split(' ')

        turn_oponent = Choice(turn_first)
        outcome = Outcome(turn_second)
        turn_mine = get_my_choice(turn_oponent, outcome)

        is_draw_turn = is_draw(turn_mine, turn_oponent)
        i_win_turn = first_win(turn_mine, turn_oponent)

        shape_score = get_shape_score(turn_mine)
        outcome_score = 0

        if i_win_turn:
            outcome_score = 6
        if is_draw_turn:
            outcome_score = 3

        total_score += shape_score + outcome_score
        #print(f'{turn_oponent=}, {turn_mine=}, {is_draw_turn=}, '
        #      f'{i_win_turn=}, {shape_score=}, {outcome_score=}')
        #break

print(total_score)
