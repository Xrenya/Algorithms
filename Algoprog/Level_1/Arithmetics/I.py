minutes = int(input())

def time(minutes):
    hour = minutes // 60
    minute = minutes % 60
    if hour >= 24:
        hour = hour - hour // 24 * 24
    return f"{hour} {minute}"

print(time(minutes))
