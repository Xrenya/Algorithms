class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        output = []
        for i in range(1, len(currentState)):
            if currentState[i - 1] == currentState[i] and currentState[i] == '+':
                output.append(currentState[:i - 1] + "--" + currentState[i + 1:])
        return output
