#include <stdio.h>

char nextGreatestLetter(char* letters, int lettersSize, char target) {
    char first = *letters;
    while (lettersSize > 0) {
        if (*letters > target) {
            return *letters;
        }
        --lettersSize;
        ++letters;
    }
    return first;
}
