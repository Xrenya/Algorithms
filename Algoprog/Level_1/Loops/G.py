number = int(input())

def divisor(number):
    for i in range(2, number+1):
        if number%i == 0:
            return i

print(divisor(number))
