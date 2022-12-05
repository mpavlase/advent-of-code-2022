from collections import namedtuple
import re

is_header = True
header = []
moves = []

Move = namedtuple('Move', ('amount', 'from_col', 'to_col'))


re_numbers = re.compile(r'(\d+).*(\d+).*(\d+)')


def parse_moves(line):
    matches = re_numbers.findall(line)
    amount, from_col, to_col = matches[0]

    amount = int(amount)
    from_col = int(from_col) - 1
    to_col = int(to_col) - 1

    return Move(amount, from_col, to_col)

def parse_header(lines):
    line_len = len(lines[0])
    columns_len = (line_len + 1) // 4
    columns = []

    for line in lines:
        for column_index, str_index in enumerate(range(1, line_len, 4)):
            if len(columns) <= column_index:
                columns.append([])
            #print(f'{columns[column_index]=}')
            #print(f'{column_index=}, {str_index=}')
            #print(f'.append({line[str_index]=}')
            char = line[str_index]
            if char == ' ':
                continue
            columns[column_index].append(char)

    return columns


with open('input') as fd:
    while True:
        line = fd.readline()
        if line == '':
            break

        if line == '\n':
            is_header = False
            header.pop(-1)
            continue

        if is_header:
            line_wo_eol = line.rstrip('\n')
            header.append(line_wo_eol)

        if not is_header:
            move = parse_moves(line)
            moves.append(move)

columns = parse_header(header)


def do_move(move_command: Move, columns):
    old_from = columns[move_command.from_col]
    old_to = columns[move_command.to_col]

    subcolumn = old_from[:move_command.amount]
    subcolumn_rev = list(reversed(subcolumn))

    new_from = old_from[move_command.amount:]
    #new_to = subcolumn_rev + old_to
    new_to = subcolumn + old_to

    columns[move_command.from_col] = new_from
    columns[move_command.to_col] = new_to

    return columns

print(columns)
for move in moves:
    columns = do_move(move, columns)
print(columns)

ret = ''
for column in columns:
    ret += column[0]

print(ret)
