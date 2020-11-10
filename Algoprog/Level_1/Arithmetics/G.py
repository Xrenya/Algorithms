digit = input()

def tens(digit):
    return int(digit[-2:]) // 10

print(tens(digit))
