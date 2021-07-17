with open('input.txt') as f:
    grade2 = int(f.readline())
    grade3 = int(f.readline())
    grade4 = int(f.readline())

def lbinsearch(grade2, grade3, grade4, checker):
    left = 0
    right = grade2 + grade3 + grade2
    while left < right:
        middle = (left + right) // 2
        if checker(grade2, grade3, grade4, middle):
            right = middle
        else:
            left = middle + 1
    return left

def checker(grade2, grade3, grade4, grade5):
    return 2 * grade2 + 3 * grade3 + 4 * grade4 + 5 * grade5 >= 3.5 * (grade2 + grade3 + grade4 + grade5)

def grader(grade2, grade3, grade4):
    min_grades = lbinsearch(grade2, grade3, grade4, checker)
    return min_grades

if __name__ == '__main__':
    size = grader(grade2, grade3, grade4)
    with open('output.txt', 'w') as file:
        file.write(f"{size}")
