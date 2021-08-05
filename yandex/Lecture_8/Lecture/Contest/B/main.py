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
            return None
        
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
        
        
def tree_levels(keys):
    bts = BTSNode()
    output = []
    for key in keys:
        if key == 0:
            break
        nownode = bts.insert_recursion(key)
        if nownode:
            output.append(nownode.level)
    return output
            
with open('input.txt') as f:
    keys = list(map(int, f.readline().split()))

if __name__ == '__main__':
    output = tree_levels(keys)
    output = list(map(str, output))
    with open('output.txt', 'w') as file:
        file.write(f"{' '.join(output)}")
