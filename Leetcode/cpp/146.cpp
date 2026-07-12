class Node {
public:
    int key;
    int value;
    Node* next = nullptr;
    Node* prev = nullptr;

    Node(int key = 0, int value = 0, Node* next = nullptr, Node* prev = nullptr)
        : key(key), value(value), next(next), prev(prev) {}
    ~Node() {}
};

class ListNode2 {
public:
    // head -> tail => old -> new
    std::unordered_map<int, Node*> map;
    Node* head = new Node(INT_MAX, INT_MAX);
    Node* tail = new Node(INT_MAX, INT_MAX);
    int capacity = 0;
    int total = 0;

    void set(int capacity = 0) {
        this->capacity = capacity;
    }
    ListNode2(int capacity = 0) : capacity(capacity) {
        head->next = tail;
        tail->prev = head;
    }

    ~ListNode2() {
        Node* cur = head;
        while (cur != nullptr) {
            Node* nextNode = cur->next;
            delete cur;
            cur = nextNode;
        }
    }

    void add(int key, int value) {
        if (map.contains(key)) {
            remove(key);
        }
        Node* node = new Node(key, value);
        Node* prevNode = tail->prev;
        prevNode->next = node;
        node->prev = prevNode;
        node->next = tail;
        tail->prev = node;
        map[key] = node;
        ++total;

        if (total > capacity) {
            Node* lru = head->next;
            remove(lru->key);
        }
    }

    void remove(int key) {
        if (!map.contains(key)) {
            return;
        }
        --total;
        Node * removeNode = map[key];
        Node * prevNode = removeNode->prev;
        Node * nextNode = removeNode->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
        map.erase(key);
        delete removeNode;
    }

    int get(int key) {
        if (!map.contains(key)) {
            return -1;
        }
        Node* node = map[key];
        int value = node->value;
        remove(key);
        add(key, value);
        return value;
    }
};

class LRUCache {
public:
    ListNode2 node;

    LRUCache(int capacity) {
        node.set(capacity);
    }
    
    int get(int key) {
        return node.get(key);
    }
    
    void put(int key, int value) {
        node.add(key, value);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
