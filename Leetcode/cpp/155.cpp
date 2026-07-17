class MinStack {
private:
    std::vector<int> main_stack;
    std::vector<int> min_stack;

public:
    MinStack() {
    }
    
    void push(int value) {
        main_stack.push_back(value);
        if (min_stack.empty() || min_stack.back() >= value) {
            min_stack.push_back(value);
        }
    }
    
    void pop() {
        if (main_stack.empty()) return;

        int value = main_stack.back();
        if (value == min_stack.back()) {
            min_stack.pop_back();
        }
        main_stack.pop_back();
    }
    
    int top() {
        return main_stack.back();
    }
    
    int getMin() {
        return min_stack.back();
    }
    
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
