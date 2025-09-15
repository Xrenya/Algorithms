#include <stdio.h>
#include <string.h>


int canBeTypedWords(char* text, char* brokenLetters) {
    int total = 0;
    char *word = strtok(text, " ");
    
    while (word != NULL) {
        total++;
        int flag = 0;
        for (int i = 0; i < strlen(brokenLetters); ++i) {
            if (strchr(word, brokenLetters[i]) != NULL) {
                flag++;
                break;
            }
        }
        total -= flag;
        // Get the next token
        word = strtok(NULL, " ");
    }
    return total;
}
