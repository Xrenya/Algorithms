# s = ":-)))((" => "(("
# s = "((:-)))((" => "(((("
# s = ":-)))" => ""


def remove(s):
    idx = 0
    output = []
    while idx < len(s):
        if idx < len(s) - 2 and s[idx] == ":" and s[idx + 1] == "-" and s[idx + 2] in ("(", ")"):
            k = idx + 2
            cur = s[idx + 2]
            while k < len(s) and cur == s[k]:
                k += 1
            idx = k
        else:
            output.append(s[idx])
            idx += 1

    return "".join(output)
