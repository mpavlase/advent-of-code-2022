a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')

offset_lowercase = a - 1
offset_uppercase = A - 27

def get_priority(char_str):
    char = ord(char_str)
    offset = 0

    if a <= char <= z:
        offset = offset_lowercase
    elif A <= char <= Z:
        offset = offset_uppercase
    else:
        raise Exception(f'unexpected char "{char_str}"')

    return char - offset


def split_compartments(rucksak):
    lenght = len(rucksak)
    assert lenght % 2 == 0

    half = lenght / 2
    half = int(half)

    return rucksak[:half], rucksak[half:]

total = 0

with open('input') as fd:
    for line in fd.readlines():
        line = line.strip()

        compartments = split_compartments(line)

        items_first = set(compartments[0])
        items_second = set(compartments[1])

        common_char = items_first.intersection(items_second)

        assert len(common_char) == 1

        total += get_priority(list(common_char)[0])

print(total)
