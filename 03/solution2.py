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
    group = []

    for line in fd.readlines():
        line = line.strip()

        group.append(line)

        if len(group) == 3:
            uniq = map(set, group)
            uniq = list(uniq)

            shared = uniq[0].intersection(uniq[1])
            shared = shared.intersection(uniq[2])

            total += get_priority(list(shared)[0])
            #print(group)
            #print(shared)

            group = []


print(total)
