#include <stdio.h>
#include <string.h>


void pprint(char s[]) {
    for (int i = 0; i < strlen(s); ++i) {
        printf("%c ", s[i]);
    }
    printf("\n");
}

void reverse(char s[]) {
    int c, i, j;
    
    for (i = 0, j = strlen(s) - 1; i < j; ++i, --j) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

int main() {
    char s[] = "abcdef";
    pprint(s);
    reverse(s);
    pprint(s);
    return 0;
}
