def search_uniq(buffer, window_size):
    for i in range(window_size, len(buffer) - 1):
        window = buffer[i - window_size:i]

        if len(set(window)) == window_size:
            return i

with open('input.sample') as fd:
    buffer = fd.read()
    print(f'{buffer=}')
    result4 = search_uniq(buffer, 4)
    print(f'{result4=}')
    result14 = search_uniq(buffer, 14)
    print(f'{result14=}')
