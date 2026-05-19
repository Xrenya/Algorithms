#include <iostream>
#include <vector>
#include <cassert>

class MyQueue {
private:
    std::vector<int> stdIn;
    std::vector<int> stdOut;

    void shiftInOut() {
        if (stdOut.empty()) {
            while (!stdIn.empty()) {
                stdOut.push_back(stdIn.back());
                stdIn.pop_back();
            }
        }
    }
public:
    MyQueue() {
        // empty
    }
    
    void push(int x) {
        stdIn.push_back(x);   
    }
    
    int pop() {
        int top = peek();
        stdOut.pop_back();
        return top;
    }
    
    int peek() {
        shiftInOut();
        return stdOut.back();
    }
    
    bool empty() {
        return stdIn.empty() && stdOut.empty();
    }
};

int main() {
    MyQueue* obj = new MyQueue();
    
    // ["MyQueue", "push", "push", "peek", "pop", "empty"]
    // [[],        [1],    [2],    [],     [],    []]
    
    obj->push(1);
    obj->push(2);
    
    int param_1 = obj->peek();
    assert(param_1 == 1 && "Test #1 (peek) failed!");
    
    int param_2 = obj->pop();
    assert(param_2 == 1 && "Test #2 (pop) failed!");
    
    bool param_3 = obj->empty();
    assert(param_3 == false && "Test #3 (empty) failed!");
    
    int param_4 = obj->pop();
    assert(param_4 == 2 && "Test #4 (pop last) failed!");
    assert(obj->empty() == true && "Test #5 (should be empty) failed!");

    delete obj;
    
    std::cout << "All tests passed successfully!" << std::endl;
    return 0;
}
