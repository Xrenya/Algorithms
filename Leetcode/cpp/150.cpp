#include <iostream>
#include <vector>
#include <cassert>
#include <climits>
#include <string>
#include <set>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        auto ops = [](int a, int b, std::string ops) {
            // if (ops == "+") {
            //     return a + b;
            // } else if (ops == "-") {
            //     return a - b;
            // } else if (ops == "*") {
            //     return a * b;
            // }
            // return a / b;
            switch (ops[0]) {
                case '+': return a + b;
                case '-': return a - b;
                case '*': return a * b;
                case '/': return a / b;   // C++ truncates toward 0 as required
            }
            return 0;
        };
        int n = static_cast<int>(tokens.size());
        std::vector<int> q;
        std::set<std::string> opsSet = {"+", "-", "*", "/"};
        for (int i = 0; i < n; ++i) {
            if (opsSet.find(tokens[i]) != opsSet.end()) {
                int b = q.back();
                q.pop_back();
                int a = q.back();
                q.pop_back();
                int c = ops(a, b, tokens[i]);
                q.push_back(c);
            } else {
                q.push_back(std::stoi(tokens[i]));
            }
        }
        return q.back();
    }
};

class SolutionV2 {
public:
    enum class Operations {
        PLUS,
        MINUS,
        MULTIPLY,
        DIVIDE
    };
    
    int evalRPN(vector<string>& tokens) {
        auto ops = [](int a, int b, Operations operation) -> int {
            switch(operation) {
                case Operations::PLUS: return a + b;
                case Operations::MINUS: return a - b;
                case Operations::MULTIPLY: return a * b;
                case Operations::DIVIDE: return a / b;
            }
        };
        std::vector<int> stack;

        for (int i = 0; i < tokens.size(); ++i) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                stack.push_back(std::stoi(tokens[i]));
            } else {
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();
                Operations current_op = Operations::PLUS;
                if (tokens[i] == "+") {
                    current_op = Operations::PLUS;
                } else if (tokens[i] == "-") {
                    current_op = Operations::MINUS;
                } else if (tokens[i] == "*") {
                    current_op = Operations::MULTIPLY;
                } else if (tokens[i] == "/") {
                    current_op = Operations::DIVIDE;
                }
                int result = ops(a, b, current_op);
                
                stack.push_back(result);
            }
        }
        return stack.back();
    }
};

int main() {
  Solution sol;
  std::vector<std::string> tokens = {"2", "1", "+", "3", "*"};
  int expected_output = 9;
  int output = sol.evalRPN(tokens);
  assert(output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
}


