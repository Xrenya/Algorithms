with open('input.txt') as f:
    output = set()
    for line in f.readlines():
        output |= set(line.split()) # Union

with open('output.txt', 'w') as f:
    f.write(str(len(output)))
