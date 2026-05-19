#include <iostream>
#include <vector>
#include <cassert>
#include <deque>

class Solution {
public:
     int countStudentsV2(std::vector<int>& students, std::vector<int>& sandwiches) {
        int n = static_cast<int>(students.size());
        std::deque<int> qStudent(students.begin(), students.end());
        std::deque<int> qSandwiches(sandwiches.begin(), sandwiches.end());
        
        int cur_iter = n;
        
        while (!qStudent.empty()) {
            int front = qStudent.front();
            qStudent.pop_front();
            int type = qSandwiches.front();
            
            if (front == type) {
                qSandwiches.pop_front();
                cur_iter = static_cast<int>(qStudent.size());
            } else {
                qStudent.push_back(front);
                --cur_iter;
            }
            
            if (cur_iter == 0) {
                break;
            }
        }
        return static_cast<int>(qStudent.size());
    }
    int countStudents(std::vector<int>& students, std::vector<int>& sandwiches) {
        int n = static_cast<int>(students.size());
        int count[2] = {0, 0};
        for (auto s : students) {
            ++count[s];
        }

        for (auto s : sandwiches) {
            if (count[s] == 0) {
                break;
            }
            --count[s];
        }

        return count[0] + count[1];
    }
};

int main() {
    Solution sol;
    std::vector<int> students = {1, 1, 0, 0};
    std::vector<int> sandwiches = {0, 1, 0, 1};
    int expected_output = 0;
    int output = sol.countStudents(students, sandwiches);
    
    assert((expected_output == output) && "Test #1 failed!");
    
    output = sol.countStudentsV2(students, sandwiches);
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
