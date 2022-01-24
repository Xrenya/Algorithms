def solution(s: str):
    right = 0
    cnt = 0
    for c in s:
        if c == "<":
            if right > 0:
                cnt += right * 2
        elif c == ">":
            right += 1

    return cnt

print(solution(">----<"), f"Correct output = {2}")
print(solution("<<>><"), f"Correct output = {4}")
print(solution("<-->"), f"Correct output = {0}")
print(solution("<<>>"), f"Correct output = {0}")
print(solution(">><<"), f"Correct output = {8}")
print(solution("<>><<>"), f"Correct output = {8}")
# s = ">----<" 2
# s = "<<>><" 4
