with open('input.txt') as f:
    nun_classes = int(f.readline())
    min_power = sorted(list(map(int, f.readline().split())))
    num_specs = int(f.readline())
    data = []
    for _ in range(num_specs):
        power, price = list(map(int, f.readline().split()))
        data.append([price, power])
        data = sorted(data)


def minimal_price(nun_classes, min_power, data):
    total_cost = 0
    i = 0
    for power in min_power:
        while i < len(data):
            conditioner_price, conditioner_power = data[i]
            if conditioner_power >= power:
                total_cost += conditioner_price
                break
            else:
                i += 1
    return total_cost



if __name__ == '__main__':
    ans = minimal_price(nun_classes, min_power, data)
    with open('output.txt', 'w') as file:
        file.write(f"{ans}")
