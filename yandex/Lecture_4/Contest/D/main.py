num_key = int(input())
max_resistance = list(map(int, input().split()))
num_pressed = int(input())
key_pressed = list(map(int, input().split()))

hash = {}
for i in range(num_key):
    hash[i+1] = max_resistance[i]
output = ["NO"] * num_key
for key in key_pressed:
    hash[key] -= 1
    if hash[key] < 0:
        output[key-1] = "YES"
print(" ".join(output))
