hour = float(input())
min = float(input())
sec = float(input())
def angle(hour, min, sec):
    return 360/12*hour+30.0*min/60+30.0/60*sec/60
angle(hour, min, sec)
