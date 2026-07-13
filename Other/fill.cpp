#include <iostream>
#include <cassert>
#include <unordered_map>


bool canFillNoOpt(int a, int b, int target) {
    if (target == 0) return true;
    if (target < 0)  return false;
    if (a == b) {
        return (canFillNoOpt(a, b, target - a) || canFillNoOpt(a, b, target - b));   
    }
    return canFillNoOpt(a, b, target - a) || canFillNoOpt(a, b, target - b) || canFillNoOpt(a, b, target - (b - a));
}


bool canFill(int a, int b, int target, std::unordered_map<int, bool>& umap) {
    if (target == 0) return true;
    if (target < 0)  return false;
    if (umap.contains(target)) {
        return umap[target];
    }
    bool result = false;
    if (a == b) {
        result = (canFill(a, b, target - a, umap) || canFill(a, b, target - b, umap));   
    } else {
        result = (canFill(a, b, target - a, umap) || canFill(a, b, target - b, umap) || canFill(a, b, target - (b - a), umap));
    }
    umap[target] = result;
    return result;
}

bool can_fill(int a, int b, int target) {
    std::unordered_map<int, bool> umap;
    return canFill(a, b, target, umap);
}

int main() {
    int a = 5, b = 3, c = 4;
    
    if (a > b) {
        std::swap(a, b);
    }
    
    bool output = can_fill(a, b, c);
    bool expectedOutput = true;
    assert((output == expectedOutput) && "Test #1 failed!");
    
    
    output = can_fill(3, 5, 8);
    expectedOutput = true;
    assert((output == expectedOutput) && "Test #2 failed!");
    
    output = can_fill(5, 5, 9);
    expectedOutput = false;
    assert((output == expectedOutput) && "Test #3 failed!");
    
    
    // no optimization
    output = canFillNoOpt(a, b, c);
    expectedOutput = true;
    assert((output == expectedOutput) && "Test #4 failed!");
    
    output = canFillNoOpt(3, 5, 8);
    expectedOutput = true;
    assert((output == expectedOutput) && "Test #5 failed!");
    
    output = canFillNoOpt(5, 5, 9);
    expectedOutput = false;
    assert((output == expectedOutput) && "Test #6 failed!");
    
    
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
