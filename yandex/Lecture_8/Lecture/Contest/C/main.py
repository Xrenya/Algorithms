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
                 
def build_tree(keys):
    bst = BST()
    for key in keys:
        if key == 0:
            break
        bst.insert(key)
    return bst

def find_second_max(node, prev_node=None, left=False):
    if node.right:
        return find_second_max(node.right, node, left)
    elif node.left and not left:
        return find_second_max(node.left, node, True)
    return node.key if left else prev_node.key

with open('input.txt') as f:
    keys = list(map(int, f.readline().split()))

if __name__ == '__main__':
    tree = build_tree(keys)
    value = find_second_max(tree)
    with open('output.txt', 'w') as file:
        file.write(f"{value}")
