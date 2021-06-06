def count_frequent_element_with_bruteforece(string: str) -> str:
    # Time complexity O(n*n)
    # Space complexity O(n)
    ans = ''
    anscnt = 0
    for i in range(len(string)):
        nowcnt = 0
        for j in range(len(string)):
            if string[i] == string[j]:
                nowcnt += 1
            if nowcnt > anscnt:
                ans = string[i]
                anscnt = nowcnt
    return ans
      
def count_frequent_element_with_bruteforece_set(string: str) -> str:
    # Time complexity O(n*k)
    # Space complexity O(n+k) = O(n)
    ans = ''
    anscnt = 0
    for now in set(string):
        nowcnt = 0
        for j in range(len(string)):
            if now == string[j]:
                nowcnt += 1
            if nowcnt > anscnt:
                ans = now
                anscnt = nowcnt
    return ans

def count_frequent_element_with_dict(string: str) -> str:
    # Time complexity O(n)
    # Space complexity O(k)
    ans = ''
    anscnt = 0
    symcnt = {}
    for now in string:
        if now not in symcnt:
            symcnt[now] = 0
        symcnt[now] += 1
        if symcnt[now] > anscnt:
            ans = now
            anscnt = symcnt[now]
    return ans


def main():
    s = 'aaaaddddcccccccccc'
    print(count_frequent_element_with_bruteforece(s))
    print(count_frequent_element_with_bruteforece_set(s))
    print(count_frequent_element_with_dict(s))


if __name__ == '__main__':
    main()
