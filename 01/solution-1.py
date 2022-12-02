total_max = 0
group_sum = 0

with open('input') as fd:
    for line in fd.readlines():
        line = line.strip()
        print(f'{line=}_')

        if line == '':
            print('current line is empty')
            if group_sum > total_max:
                total_max = group_sum

            group_sum = 0
            continue

        number = int(line)
        group_sum += number

print(total_max)
