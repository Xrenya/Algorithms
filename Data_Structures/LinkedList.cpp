#include <iostream>
#include <format>
#include <string>
// std::forward_list

class Node {
public:
    double data;
    Node * next;

public:
    Node(double data = 0.0) {
        this->data = data;
        this->next = nullptr; // NULL
    }
    
};

class OneLinkedList {
public:
    Node * head, * tail;

public:
    OneLinkedList() {
        this->head = nullptr;
        this->tail = nullptr;
    }
    ~OneLinkedList() {
        while (head != nullptr) {
            pop_front();
        }
    }
    
    void pop_front() {
        if (head == nullptr) return;
        if (head == tail) {
            delete tail;
            head = tail = nullptr;
            return;
        }
        Node * nextNode = head->next;
        delete head;
        head = nextNode;
    }
    
    void push_back(double delta) {
        Node * node = new Node(delta);
        if (head == nullptr) {
            head = node;
        }
        if (tail != nullptr) {
            tail->next = node;
        }
        tail = node;
    }
    
    void push_front(double delta) {
        Node * node = new Node(delta);
        node->next = head;
        head = node;
    }
    
    void pop_back() {
        if (tail == nullptr) return;
        if (head == tail) {
            delete tail;
            head = tail = nullptr;
            return;
        }
        Node * node = head;
        while (node->next != tail) {
            node = node->next;
        }
        delete tail;
        tail = node;
        node->next = nullptr;
    }
    
    Node * getAt(int k) {
        if (k < 0) return nullptr;
        Node * node = head;
        for ( ; node != nullptr, k > 0; node = node->next, --k) { }
        if (k == 0) {
            return node;
        }
        return nullptr;
    }
    
    void insert(int k, double data) {
        Node * left = getAt(k);
        if (left == nullptr) return;
        Node * right = left->next;
        Node * node = new Node(data);
        left->next = node;
        node->next = right;
        if (right == nullptr) {
            tail = node;
        }
    }
    
    void erase(int k) {
        if (k < 0) return;
        if (k == 0) {
            pop_front();
            return;
        }
        Node * left = getAt(k - 1);
        Node * node = left->next;
        if (node == nullptr) return;
        Node * right = node->next;
        
        left->next = right;
        if (node == tail) tail = left;
        delete node;
    }
    
    void pprint() {
        if (head == nullptr) return;
        Node * node = head;
        while (node) {
            std::string message = "";
            if (node->next != nullptr) {
                message = std::format("Node({})->", node->data);
            } else {
                message = std::format("Node({})", node->data);
            }
            std::cout << message;
            node = node->next;
        }
        std::cout << std::endl;
    }
};

int main() {
    OneLinkedList forward_list;
    int ar[5]{1, 2, 3, 4, 5};
    for (int i = 0; i < sizeof(ar) / sizeof(ar[0]); ++i) {
        forward_list.push_back(ar[i]);
    }
    forward_list.erase(0);
    forward_list.pprint(); // Node(2)->Node(3)->Node(4)->Node(5)
    std::cout << forward_list.getAt(0)->data << std::endl; // 2
    forward_list.insert(1, 0.5); // Node(2)->Node(3)->Node(0.5)->Node(4)->Node(5)
    forward_list.pprint();
    return 0;
}
