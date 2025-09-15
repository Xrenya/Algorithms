#include <iostream>
#include <string>
#include <sstream>
#include <unordered_set>


class Solution {
public:
    int canBeTypedWordsV1(std::string text, std::string brokenLetters) {
        int count = 0;
        char *cText = new char[text.size() + 1];
        std::strcpy(cText, text.c_str());

        char *word = std::strtok(cText, " ");
        while (word != nullptr) {
            bool canType = true;
            for (char broken : brokenLetters) {
                if (std::strchr(word, broken) != nullptr) {
                    canType = false;
                }
            }
            if (canType) {
                count++;
            }
            word = std::strtok(nullptr, " ");
        }
        return count;
    }
};


class Solution {
public:
    int canBeTypedWordsV2(std::string text, std::string brokenLetters) {
        std::unordered_set<char> broken(brokenLetters.begin(), brokenLetters.end());
        std::istringstream iss(text);
        std::string word;
        int counter = 0;
        // iss parse till white space
        while (iss >> word) {
            bool bad = false;
            for (char c : word) {
                if (broken.count(c)) {
                    bad = true;
                    break;
                }
            }
            if (!bad) {
                counter++;
            }
        }
        return counter;
    }
};
