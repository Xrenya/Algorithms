#include <iostream>
#include <queue>
#include <unordered_set>
#include <string>
#include <vector>


class PhoneDirectory {
private:
    int maxNumbers;
    int nextAvailable;
    std::queue<int> released;
    std::unordered_set<int> used;

public:
    PhoneDirectory(int maxNumbers) : maxNumbers(maxNumbers), nextAvailable(0) {}

    int get() {
        if (nextAvailable < maxNumbers) {
            used.insert(nextAvailable);
            return nextAvailable++;
        }
        if (!released.empty()) {
            int num = released.front();
            released.pop();
            used.insert(num);
            return num;
        }
        return -1;
    }

    bool check(int number) {
        return used.find(number) == used.end();
    }

    void release(int number) {
        if (used.find(number) != used.end()) {
            used.erase(number);
            released.push(number);
        }
    }
};


int main() {
	std::vector<std::string> cmd = {"PhoneDirectory","get","get","check","get","check","release","check"};
	std::vector<int> values = {3,-1,-1,2,-1,2,2,2};
	PhoneDirectory sol(values[0]);
    std::cout << "null" << ",";
	// expected output [null,0,1,true,2,false,null,true]
	for (int i = 1; i < values.size(); ++i) {
        if (cmd[i] == "get") {
            std::cout << sol.get() << ",";
        } else if (cmd[i] == "check") {
            std::cout << (sol.check(values[i]) ? "true" : "false") << ",";
        } else {
            sol.release(values[i]);
            std::cout << "null" << ",";
        }
	}
	
	return 0;

}
