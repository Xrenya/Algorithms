#include <iostream>
#include <queue>

using namespace std;

class MRUQueue {
private:
    vector<int> queue;

public:
    MRUQueue(int n) {
        for (int i = 1; i <= n; ++i) {
            queue.push_back(i);
        }
    }
    
    int fetch(int k) {
        int val = queue[k - 1];
        queue.erase(queue.begin() + k - 1);
        queue.push_back(val);
        return val;
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */
