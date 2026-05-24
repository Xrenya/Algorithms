#include <iostream>
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>
#include <memory>

class Node {
public:
    int val;
    Node* next;
    Node* prev;

    Node(int v = 0) : val(v), next(nullptr), prev(nullptr) {}
};

class MyCircularQueue {
private:
    Node* dummy;
    int maxSize;
    int curSize;

public:
    explicit MyCircularQueue(int k)
        : dummy(new Node(-1)), maxSize(k), curSize(0)
    {
        dummy->next = dummy;
        dummy->prev = dummy;
    }

    ~MyCircularQueue() {
        while (!isEmpty()) {
            deQueue();
        }
        delete dummy;
    }

    MyCircularQueue(const MyCircularQueue&) = delete;
    MyCircularQueue& operator=(const MyCircularQueue&) = delete;

    bool enQueue(int value) {
        if (isFull()) return false;

        Node* add = new Node(value);
        Node* oldRear = dummy->next;

        add->prev = dummy;
        add->next = oldRear;

        oldRear->prev = add;
        dummy->next = add;

        ++curSize;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;

        Node* frontNode = dummy->prev;
        Node* newFront = frontNode->prev;

        newFront->next = dummy;
        dummy->prev = newFront;

        if (frontNode == dummy->next) {
            dummy->next = dummy;
        }

        delete frontNode;
        --curSize;
        return true;
    }

    int Front() const {
        return isEmpty() ? -1 : dummy->prev->val;
    }

    int Rear() const {
        return isEmpty() ? -1 : dummy->next->val;
    }

    bool isEmpty() const {
        return curSize == 0;
    }

    bool isFull() const {
        return curSize == maxSize;
    }
};


int main() {
    int size = 3;
    MyCircularQueue q(size);
    std::vector<int> vec = {1, 2, 3, 5, 2};
    for (int i = 0; i < vec.size(); ++i) {
        bool expectedOutput = i < size ? true : false;
        assert((expectedOutput == q.enQueue(vec[i])) && "Test `enQueue` failed!");
    }
    int intFront = 1;
    int intRear = 3;
    assert((intFront == q.Front()) && "Test `Front` failed!");
    assert((intRear == q.Rear()) && "Test `intRear` failed!");
    assert((false == q.isEmpty()) && "Test `isEmpty` failed!");
    assert((true == q.isFull()) && "Test `isFull` failed!");
    
    
    for (int i = 0; i < size; ++i) {
        q.deQueue();
    }
    
    assert((false == q.isFull()) && "Test `isFull` failed!");
    assert((true == q.isEmpty()) && "Test `isEmpty` failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
