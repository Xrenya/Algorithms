int appendCharacters(char* s, char* t) {
    while (*s) {
        if (*t == *s++) {
            t++;
        }
        if (*t == 0) {
            return 0;
        }
    }
    char *st = t;
    while (*t) {
        t++;
    }
    return t- st;
}
