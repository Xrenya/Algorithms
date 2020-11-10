rub = int(input())
kop = int(input())
num = int(input())

def price(rub, kop, num):
    rubles = rub * num
    kops = kop * num
    if kops >= 100:
        rubles += kops // 100
        kops = kops - kops // 100 * 100
    return f"{rubles} {kops}"

print(price(rub, kop, num))
