from bst import BinarySearchTree
import random
nodes = []

def height(tree: BinarySearchTree) -> int:
    l: int = 0
    r: int = 0
    if tree is None:
        return 0
    else:
        l = height(tree.left)
        r = height(tree.right)
        if l > r:
            return l + 1
        else:
            return r + 1

def get_layer_nodes(tree: BinarySearchTree, depth: int) -> None:
    
    if tree is None:
       return
    
    if depth == 1:
        nodes.append(tree)
    
    elif depth > 1:
        get_layer_nodes(tree.left, depth - 1)
        get_layer_nodes(tree.right, depth - 1)





def main():
    
    root = BinarySearchTree(random.randint(0, 20))
    for _ in range(10):
        root.insert(BinarySearchTree(random.randint(0, 20)))
    root.display()
    
    h = height(root)
    get_layer_nodes(root, h)
    s = 0
    
    for node in nodes:
        s += node.key
        print(node.key)
    print("sum of deapest leaves: ", s)
if __name__ == '__main__':
    main()
