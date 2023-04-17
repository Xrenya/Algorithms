# Function to print all combinations of phrases that can be formed
# by words from each of the given lists

sents = [
    ["you", "we", "he"],
    ["have", "are", "do"],
    ["sleep", "eat", "drink"]
]
output = []

def recursive_add(sents, sent = [], index: int = 0):
    if index == len(sents):
        output.append(" ".join(sent[:]))
        return
    
    for word in sents[index]:
        sent.append(word)
        recursive_add(sents, sent, index + 1)
        sent.pop()
        
recursive_add(sents)

print(output)
