class BST:
    def __init__(self, key=None, height=1):
        self.key = key
        self.left = None
        self.right = None
        self.height = height

    def insert(self, key):
        if self.key is None:
            self.key = key
            return self
        elif self.key < key:
            if self.right:
                return self.right.insert(key)
            self.right = BST(key, self.height + 1)
            return self.right
        else:
            if self.left:
                return self.left.insert(key)
            self.left = BST(key, self.height + 1)
            return self.left

    def search(self, key):
        if self.key is None:
            return False
        elif self.key == key:
            return True
        elif self.key < key:
            if self.right:
                return self.right.search(key)
            else:
                return False
        elif self.key > key:
            if self.left:
                return self.left.search(key)
            else:
                return False

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node


bst = BST()
nums = [6,4,9,1,5,8,10]
#    H=1                  6
#    H=2          4              9
#    H=3       1     5        8     10
max_height = 0
for num in nums:
    node_height = bst.insert(num)
    if max_height < node_height.height:
        max_height = node_height.height
        print(max_height)
print("____")


def find_max_value(node):
    if node.right:
        return find_max_value(node.right)
    return node.key

print("Maximum value in tree: ", find_max_value(bst))

def find_second_max_value(node, prev=None, left=False):
    if node.right:
        return find_second_max_value(node.right, prev=node, left=False)
    if node.left and not left:
        return find_second_max_value(node.right, prev=node, left=True)
    return node.key if left else prev.key

print("The second maximum value in tree: ", find_second_max_value(bst))

searches = [6, 4, 5, 9, 0, 1]
for search in searches:
    print(bst.search(search))

print([node.key for node in bst])
