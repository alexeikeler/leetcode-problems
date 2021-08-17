from bst import BinarySearchTree
from typing import List
#variables for first solution
nodes = []
without_last_layer = []
almost_last = []








def print_level_order(tree: BinarySearchTree) -> None:
    h = height(tree)
    print(h)
    for i in range(1, h+1):
        print_current_level(tree, i)

def print_current_level(node: BinarySearchTree, level: int) -> None:
    
    if node is None:
        return
    
    if level == 1:
        nodes.append(node)
        
        
        #print(f"({node.key}, {node.value})")
        
    elif level > 1:
        without_last_layer.append(node)
        
        
        if level - 1 == 1:
            almost_last.append(node)
        print_current_level(node.left, level - 1)
        print_current_level(node.right, level - 1)
     
        

def completeness(nodes: List) -> bool:
    
    for i in range(len(nodes)):
        
        if (nodes[i].left is None) and (nodes[i].right is None) and(i == len(nodes)-1):
            return True
        
        elif nodes[i].left is None:
            return False
        elif (nodes[i].right is None) and (i != len(nodes)-1):
            print(i, len(nodes))
            return False
        

    return True
            
        

def height(node: BinarySearchTree) -> int:
    lheight: int = 0
    rheight: int = 0

    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def main():
    root = BinarySearchTree(19, "")
    node = BinarySearchTree(10, "")
    node1 = BinarySearchTree(4, "")
    node11 = BinarySearchTree(20, "")
    node111 = BinarySearchTree(13, "")
    
    
   # node6 = BinarySearchTree(81, "")
    root.insert(node)
    root.insert(node1)
    root.insert(node11)
    root.insert(node111)
    


    root.display()
    h = height(root)
    print("height of tree: ", h)
    
    print_current_level(root, h)



    print("node keys list without last layer: ")
    for node in without_last_layer:
        print(node.key)
    
    print("pre last layer")
    for node in almost_last:
        print(node.key)

    print("params: ", len(without_last_layer), ( 2**(h-1) )-1)


    neg = "It's not a complete BST"
    pos = "It's a complete BST"

    if len(without_last_layer) != (2**(h-1)) - 1:
        print(neg, "~~~")
    else:
        is_complete = completeness(almost_last)
        if is_complete:
            print(pos)
        else:
            print(neg)

if __name__ == '__main__':
    main()
    