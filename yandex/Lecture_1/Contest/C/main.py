phone = str(input())
first = str(input())
second = str(input())
third = str(input())
def check(phone=phone, first=first,
          second=second, third=third):
    phone = (clean(phone))
    first = clean(first)
    second = clean(second)
    third = clean(third)
    print_out(phone, first)
    print_out(phone, second)
    print_out(phone, third)

def clean(string):
    string = string.replace("-", "").replace("(", "").replace(")", "")
    if len(string) == 7:
        return "8495" + string
    if string.startswith("+7"):
        string = "8" + string[2:]
    return string

def print_out(phone, comparison):
    if phone == comparison:
        print("YES")
    else:
        print("NO")

check(phone=phone, first=first,
      second=second, third=third)
