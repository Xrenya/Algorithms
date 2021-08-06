class BTSNode:
    def __init__(self, key=None, level=1):
        self.key = key
        self.level = level
        self.left = None
        self.right = None
    
    def insert_recursion(self, key):
        if self.key is None:
            self.key = key
            return self
        
        if key == self.key:
            return self
        
        elif key < self.key:
            if self.left:
                return self.left.insert_recursion(key)
            self.left = BTSNode(key=key, level=self.level+1)
            return self.left
        
        else:
            if self.right:
                return self.right.insert_recursion(key)
            self.right = BTSNode(key=key, level=self.level+1)
            return self.right
        
        
def tree_height(keys):
    bts = BTSNode()
    max_level = 0
    for key in keys:
        if key == 0:
            break
        nownode = bts.insert_recursion(key)
        if nownode.level > max_level:
            max_level = nownode.level
    return max_level
            
with open('input.txt') as f:
    keys = list(map(int, f.readline().split()))

if __name__ == '__main__':
    height = tree_height(keys)
    with open('output.txt', 'w') as file:
        file.write(f"{height}")
