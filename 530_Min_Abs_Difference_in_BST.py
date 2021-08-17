from bst import  BinarySearchTree
import random
keys = []
import math

def lpr(tree: BinarySearchTree) -> None:
    if tree != None:
       lpr(tree.left)
       keys.append(tree.key)
       lpr(tree.right) 

def lpr_iterative(tree, keys_):
    if tree is None:
        return
    
    st = []
    current = tree

    while (len(st) or current != None):
        while(current != None):
            keys_.append(current.key)
            if current.right != None:
                st.append(current.right)
            current = current.left
        if len(st) > 0:
            current = st[-1]
            st.pop()


def min_distance(keys_) -> None:
    l = len(keys_)
    min_dist = math.inf
    keys_.sort()
    for i in range(l-1):
        k = abs(keys_[i] - keys_[i+1])
        if k < min_dist:
            min_dist = k
        
    print("min dist: ", min_dist)
            

def main():
    root = BinarySearchTree(random.randint(1, 50))
    for _ in range(5):
        root.insert(BinarySearchTree(random.randint(1, 50)))
    root.display()

    #lpr(root)
    keys_ = []
    lpr_iterative(root, keys_)
    print("lpriter:", keys_)

    min_distance(keys_)

if __name__== '__main__':
    main()