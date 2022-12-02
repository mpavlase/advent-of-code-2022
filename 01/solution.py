groups_max = []
group_sum = 0


with open('input') as fd:
    for line in fd.readlines():
        line = line.strip()

        if line == '':
            groups_max.append(group_sum)
            group_sum = 0
            continue

        number = int(line)
        group_sum += number

top3 = sorted(groups_max, reverse=True)[:3]
print(top3)
print(sum(top3))
