#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>

class Solution {
public:
    std::string reformatDate(std::string date) {
        int n = static_cast<int>(date.size());
        std::vector<std::string> months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        std::string day, month, year;
        int i = 0;
        for ( ; i < 2; ++i) {
            if (!std::isdigit(date[i])) {
                break;
            }
        }
        day = date.substr(0, i);
        int start = i;
        int firstSpace = 0;
        for ( ; i < n; ++i) {
            if (date[i] == ' ') {
                ++firstSpace;
                if (firstSpace == 1) {
                    start = i + 1;
                } else if (firstSpace == 2) {
                    break;
                }
            }
        }
        for (int j = 0; j < months.size(); ++j) {
            if (date.substr(start, i - start) == months[j]) month = std::to_string(j + 1);
        }
        if (month.length() == 1) month = '0' + month;
        if (day.length() == 1) day = '0' + day;
        year = date.substr(i + 1, n - i - 1);
        std::string output = year + '-' + month + '-' + day;
        return output;
    }
};

int main() {
    Solution sol;
    std::string date = "20th Oct 2052";
    std::string expectedOutput = "2052-10-20";
    std::string output = sol.reformatDate(date);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
