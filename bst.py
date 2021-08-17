

class BinarySearchTree:
    
    def __init__(self, key): 
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def search(self, key):
        try:
            if self == None or key == self.key:
                return self
            
            elif key < self.key:
                return self.left.search(key)
    
            else:
                return self.right.search(key)
        except:
            return None
        
    
    def find_min(self, node):
        while node.left != None:
            node = node.left
        return node

    
    def find_max(self, node):
        while node.right != None:
            node = node.right
        return node

   
    def succsessor(self, node):
        
        try:   
            if node.right != None:
                return self.find_min(node.right)
            y = node.parent 
            while y != None and node == y.right:
                node = y
                y = y.parent
            return y 
        
        except:
            return None
    
    
    def predecessor(self, node):
       
        try:
           if node.left != None:
               return self.find_max(node.left)
           y = node.parent
           while y != None and node == y.left:
               node = y
               y = y.parent
           return y
    
        except:
            return None
        

    def insert(self, node):

        tmp = None
        root = self
        
        while root != None:
            tmp = root
            if node.key < root.key:
                root = root.left
            else:
                root = root.right
                
        node.parent = tmp
        if tmp == None:
            self = node
        elif node.key < tmp.key:
            tmp.left = node
        else:
            tmp.right = node       
    

    def delete(self, node):
        y = None
        
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            y == self.find_min(self)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
                
                
    def transplant(self, sub_tree_1, sub_tree_2):
        
        if sub_tree_1.parent == None:
            self = sub_tree_2
        elif sub_tree_1 == sub_tree_1.parent.left:
            sub_tree_1.parent.left = sub_tree_2
        else:
            sub_tree_1.parent.right = sub_tree_2
            
        if sub_tree_2 != None:
            sub_tree_2.parent = sub_tree_1.parent
        
    def left_rotate(self, node):
        
        root = self
        y = node.right
        node.right = y.left

        if y.left != None:
            y.left.parent = node
        y.parent = node.parent
        if y.parent == None:
            root = y
        elif y == y.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):

        root = self
        y = node.left
        node.left = node.parent

        if y.right != None:
            y.right.parent = node
        y.parent = node.parent
        if y.parent == None:
            root = y
        elif y == y.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y



    def in_order_walk(self, node):

        if node != None:
            self.in_order_walk(node.left)
            print(node.key)
            self.in_order_walk(node.right)


    def pre_order_walk(self, node):

        if node != None:
            print(node.key)
            self.pre_order_walk(node.left)
            self.pre_order_walk(node.right)


    def display(self):
        lines, *_ = self.fancy_output()
        for line in lines:
            print(line)


    def fancy_output(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % f"{self.key}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.fancy_output()
            s = '%s' % f"{self.key}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.fancy_output()
            s = '%s' % f"{self.key}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.fancy_output()
        right, m, q, y = self.right.fancy_output()
        s = '%s' % f"{self.key}"
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

