with open('input.txt') as f:
    nun_classes = int(f.readline())
    min_power = list(map(int, f.readline().split()))
    num_specs = int(f.readline())
    data = {}
    for _ in range(num_specs):
        power, price = list(map(int, f.readline().split()))
        if power not in data:
            data[power] = price
        elif power in data:
            if data[power] > price:
                data[power] = price


def minimal_price(nun_classes, min_power, data):
    output = 0
    spec_range = sorted(data.keys())
    for i in range(nun_classes):
        nowprice = 1001
        for spec in spec_range:
            if min_power[i] <= spec:
                if data[spec] < nowprice:
                    nowprice = data[spec]
        output += nowprice
    return output

if __name__ == '__main__':
    ans = minimal_price(nun_classes, min_power, data)
    with open('output.txt', 'w') as file:
        file.write(f"{ans}")
