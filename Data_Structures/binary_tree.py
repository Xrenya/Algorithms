class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

class Tree:
    def __init__(self):
        self.root = None
        
    def _find(self, node, parent, value):
        if node is None:
            return node, parent, False
            
        if value == node.data:
            return node, parent, True
            
        if value < node.data:
            if node.left:
                return self._find(node.left, node, value)
            return node, parent, False  # Возвращаем текущий узел как потенциального родителя
                
        if value > node.data:
            if node.right:
                return self._find(node.right, node, value)
            return node, parent, False  # Возвращаем текущий узел как потенциального родителя
                
        return node, parent, False
    
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
            
        s, p, fl_find = self._find(self.root, None, obj.data)
        
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        
        return obj
    
    def show_tree(self, node):
        if node is None:
            return
        
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)
    
    def _del_leaf(self, s, p):
        if p is None:  # Если удаляем единственный корень-лист
            self.root = None
        elif p.left == s:
            p.left = None
        else:
            p.right = None
    
    def _del_one_child(self, s, p):
        # Находим, какой именно потомок есть у узла s
        child = s.left if s.left is not None else s.right
        
        if p is None:  # Если удаляем корень, у которого только один потомок
            self.root = child
        elif p.left == s:
            p.left = child
        else:
            p.right = child
    
    def _find_min(self, node, parent):
        if node.left:
            return self._find_min(node.left, node) # Исправлено имя метода
        return node, parent
       
    def del_node(self, key):
        s, p, fl_find = self._find(self.root, None, key) # Исправлено obj.data на key
        
        if not fl_find:
            return None
            
        # Случай 1: Узел — лист
        if s.left is None and s.right is None:
            self._del_leaf(s, p)
            
        # Случай 2: У узла только один потомок
        elif s.left is None or s.right is None:
            self._del_one_child(s, p)
            
        # Случай 3: У узла два потомка
        else:
            sr, pr = self._find_min(s.right, s)
            s.data = sr.data
            # Правый минимальный узел (sr) гарантированно имеет не более 1 потомка (правого)
            if sr.left is None and sr.right is None:
                self._del_leaf(sr, pr)
            else:
                self._del_one_child(sr, pr)
    
    def show_level_tree(self, node):
        if node is None:
            return
        
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn.append(x.left)
                if x.right:
                    vn.append(x.right)
            print()
            v = vn
            
# Проверка работы
v = [10, 5, 7, 16, 13, 2, 20]
t = Tree()
for x in v:
    t.append(Node(x))

print("Дерево до удаления:")
t.show_tree(t.root)
print("\n")
t.show_level_tree(t.root)

# Проверяем удаление узла с двумя потомками (например, 5)
t.del_node(5)

print("\nДерево после удаления узла 5:")
t.show_tree(t.root)
print("\n")
t.show_level_tree(t.root)
