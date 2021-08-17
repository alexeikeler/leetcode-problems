from bst import BinarySearchTree as BST
import random

def delete(node: BST, key: int) -> None:
    
    if not node:
        return
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if not node.left:
            return node.right
        else:
            tmp = node.left
            while tmp.right:
                tmp = tmp.right
            node.key = tmp.key
            node.left = delete(node.left, tmp.key)
    return node
        




def main():
    tree = BST(12)
    for _ in range(5):
        tree.insert(BST(random.randint(0, 23)))
    tree.display()

    key = int(input("Key: "))
    delete(tree, key)
    print("tree after deleting node with given key\n")
    tree.display()

if __name__ == '__main__':
    main()
 