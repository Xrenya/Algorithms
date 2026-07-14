class RandomizedSet {
    std::vector<int> stack;
    std::unordered_map<int, int> umap;


    std::random_device rd;
    std::mt19937 gen; ;

public:
    RandomizedSet() : gen(rd()) {
    }
    
    bool insert(int val) {
        if (umap.contains(val)) {
            return false;
        }
        umap[val] = stack.size();
        stack.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (!umap.contains(val)) {
            return false;
        }
        int removeIndex = umap[val];
        int lastElement = stack.back();
        
        stack[removeIndex] = lastElement;
        umap[lastElement] = removeIndex;
        
        stack.pop_back();
        umap.erase(val);
        return true;
    }
    
    int getRandom() {
        std::uniform_int_distribution<int> distrib(0, stack.size() - 1);
        return stack[distrib(gen)];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
