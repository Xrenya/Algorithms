import random

# probs = [0.1, 0.4, 0.2, 0.3]
# size = 7
# random.random() ~ U(0, 1)


def prefix(probs):
    proba = probs.copy()
    for i in range(1, len(probs)):
        proba[i] += proba[i - 1]
    return proba

def weighted_choice(probs, size):
    p = prefix(probs)
    output = []
    for i in range(size):
        proba = random.random()
        for i in range(len(p)):
            if proba <= p[i]:
                output.append(i)
                break
    return output
