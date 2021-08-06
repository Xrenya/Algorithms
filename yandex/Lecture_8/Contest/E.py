class BST:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.key is None:
            self.key = val
            return self

        elif self.key == val:
            return self

        elif self.key < val:
            if self.right:
                return self.right.insert(val)
            self.right = BST(key=val)
            return self.right

        else:
            if self.left:
                return self.left.insert(val)
            self.left = BST(key=val)
            return self.left

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node
                 
def build_tree(keys):
    bst = BST()
    for key in keys:
        if key == 0:
            break
        bst.insert(key)
    return bst

def traverse(bst):
    results = []
    for node in bst:
        if not node.left and not node.right:
            results.append(node.key)
    return results

with open('input.txt') as f:
    keys = list(map(int, f.readline().split()))

if __name__ == '__main__':
    tree = build_tree(keys)
    value = traverse(tree)
    value = list(map(str, value))
    with open('output.txt', 'w') as file:
        for val in value:
            file.write(val + "\n")
