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

    def remove(self, key):
        """Delete node and balance the tree
        Case 1: not left or right child
        Case 2: has one left or right child
        Case 3: has left and right child
        :param key:
        :return:
        """
        if self.key == key:
            # print(self.key, self.right, self.left)
            # does not remove root value
            if self.right and self.left: # Case 3
                [psucc, succ] = self.right._findMin(self)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                succ.left = self.left
                succ.right = self.right

                return succ
            elif self.left: # Case 2
                return self.left
            else: # Case 2
                return self.right
        elif self.key < key:
            if self.right:
                self.right = self.right.remove(key)
        elif self.key > key:
            if self.left:
                self.left = self.left.remove(key)
        return self

    def _findMin(self, parent):
        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

bst = BST()
nums = [6,4,9,1,0,5,8,10]
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


def in_order(node, array):
    if node:
        in_order(node.left, array)
        array.append(node.key)
        in_order(node.right, array)
        return array


def post_order(node, array):
    if node:
        post_order(node.left, array)
        post_order(node.right, array)
        array.append(node.key)
        return array

def pre_order(node, array):
    if node:
        array.append(node.key)
        pre_order(node.left, array)
        pre_order(node.right, array)
        return array


print("In order")
array = []
array = in_order(bst, array)
print(array)
print("In order: finished")
bst.display()
bst.remove(9)
bst.display()
print("In order")
array = []
array = in_order(bst, array)
print(array)
print("In order: finished")


print("In post_order")
array = []
array = post_order(bst, array)
print(array)
print("In post_order: finished")

print("In pre_order")
array = []
array = pre_order(bst, array)
print(array)
print("In pre_order: finished")

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
