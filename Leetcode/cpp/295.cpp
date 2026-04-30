#include <iostream>
#include <vector>
#include <cassert>
#include <queue>

class MedianFinder {
private:
    std::priority_queue<int> maxHeap; // lower half
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap; // upper half

public:
    MedianFinder() {}
    
    void addNum(int num) {
        maxHeap.push(num);

        minHeap.push(maxHeap.top());
        maxHeap.pop();

        if (maxHeap.size() < minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.top();
        }
        return (minHeap.top() + maxHeap.top()) / 2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

int main() {
    MedianFinder sol;
    std::vector<int> input = {1, 2, -1, 3, -1};
    std::vector<double> output = {1.5, 2.0};
    int index = 0;
    for (auto val : input) {
        if (val > 0) {
            sol.addNum(val);
        } else {
            double expected_output = sol.findMedian();
            assert(output[index++] == expected_output && "Test #1 failed!");
        }
    }

    std::cout << "Tests are passed!\n";
    return 0;
}
