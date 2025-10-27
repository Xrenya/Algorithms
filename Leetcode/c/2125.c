int numberOfBeams(char** bank, int bankSize) {
    int output = 0, prev = 0;;
    for (int i = 0; i < bankSize; ++i) {
        int count = 0;
        for (int j = 0; j < strlen(bank[i]); ++j) {
            if (bank[i][j] == '1') {
                count++;
            }
        }
        if (count > 0) {
            output += (prev * count);
            prev = count;
        }
    }
    return output;
}
