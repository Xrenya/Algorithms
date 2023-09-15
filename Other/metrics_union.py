# Two list of search docx indexs are given
# Calculate the top-N for the two equal len list
# e.g.
# [1, 1, 2, 3], [2, 1, 3, 1] -> [0, 1, 2, 3]
# [1, 1, 1, 3], [3, 2, 2, 2] -> [0, 0, 0, 1]

def metrics_prefix_non_optimal(a, b):
    # Complexity O(n**2)
    output = []
    for i in range(len(a)):
        left_set = set(a[:i + 1])
        right_set = set()
        count = 0
        for j in range(i, len(b)):
            if b[j] in left_set and b[j] not in right_set:
                count += 1
            right_set.add(b[j])
        output.append(count)
    return output

def metrics_prefix_extra_space(a, b):
    # Complexity O(n)
    # Extra space is used, solve without union set
    output = []
    left_set = set()
    right_set = set()
    union = set()
    for i in range(len(a)):
        right_set.add(b[j])
        left_set.add(a[j])
        if a[i] in right and a[i] not in union:
            count += 1
            union.add(a[i])
        if b[i] in left and b[i] not in union:
            count += 1
            union.add(a[i])
        output.append(count)
    return output

def metrics_prefix_optimal(a, b):
    # Complexity O(n)
    # Only two set is used
    output = []
    left_set = set()
    right_set = set()
    for i in range(len(a)):
        if a[i] not in left and a[i] in right_set:
            count += 1
        left_set.add(a[j])
        
        if b[i] not in right and b[i] in left_set:
            count += 1
        right_set.add(b[j])
        
        output.append(count)
    return output
