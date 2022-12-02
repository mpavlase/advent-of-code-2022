# oponent ABC - rock, paper, scissors
# mine XYZ - rock, paper, scissors

from enum import Enum

class Choice(Enum):
    rock = 'A'
    paper = 'B'
    scissors = 'C'

def first_win(first, second):
    situations = [
        (Choice.rock, Choice.scissors),
        (Choice.paper, Choice.rock),
        (Choice.scissors, Choice.paper)
    ]

    return (first, second) in situations


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


total_score = 0


with open('input') as fd:
    for line in fd.readlines():
        line = line.strip()

        turn_oponent, turn_mine = line.split(' ')

        turn_oponent = Choice(turn_oponent)
        turn_mine = translate_mine_to_oponent(turn_mine)

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
