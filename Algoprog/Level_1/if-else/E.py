year = int(input())

def leap(year):
    if (year%4 == 0) and not (year%100 != 0) and (year%400 == 0):
        return "YES"
    else:
        return "NO"
    
print(leap(year))
