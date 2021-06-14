def freq(hash, word):
    if word not in hash:
        hash[word] = 0
        return hash[word]
    else:
        hash[word] += 1
        return hash[word]

with open('input.txt') as file:
    hash = {}
    output = []
    for line in file.readlines():
        words = list(line.split())
        for word in words:
            output.append(freq(hash, word))

with open('output.txt', 'w') as file:
    output = [str(out) for out in output]
    file.write(" ".join(output))
