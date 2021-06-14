with open('input.txt') as file:
    hash = {}
    for line in file.readlines():
        name, product, quant = list(line.split())
        if name not in hash:
            hash[name] = {}
        if product not in hash[name]:
             hash[name][product] = 0
        hash[name][product] += int(quant)
            
with open('output.txt', 'w') as file:
    for key in sorted(hash.keys()):
        file.write(f"{key}:\n")
        for p in sorted(hash[key].keys()):
            file.write(f"{p} {hash[key][p]}\n")
