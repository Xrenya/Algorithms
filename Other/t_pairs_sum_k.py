arr = [2, 4, 5, 3]
k = 7
output = []
mapping = {}
for a in arr:
    if  (k - a) in mapping:
        output.append((k - a, a))
    mapping[a] = 0
    
print(output)
