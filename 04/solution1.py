from collections import namedtuple

Range = namedtuple('Range', ('begin', 'end'))

def convert_str_to_range(input_str):
    str_begin, str_to = input_str.split('-')
    return Range(int(str_begin), int(str_to))

def is_first_in_second(first, second):
    return (second.begin <= first.begin <= second.end and
            second.begin <= first.end <= second.end)


count = 0
with open('input') as fd:
    while True:
        line = fd.readline()

        if line == '':
            break

        line = line.strip()

        first, second = line.split(',')
        first = convert_str_to_range(first)
        second = convert_str_to_range(second)

        fist_is_in = is_first_in_second(first, second)
        second_is_in = is_first_in_second(second, first)

        if fist_is_in or second_is_in:
            count += 1

        #print(f'{line=}, {fist_is_in=}, {second_is_in=}')

print(count)
