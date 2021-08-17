from bst import BinarySearchTree as BST
flag = True
counter1 = 0
counter2 = 0

class Solution:
    def __init__(self, tree:BST, sub_tree: BST) -> None:
        self.tree = tree
        self.sub_tree = sub_tree
    
    
    
    def find_sub_tree(self, tree: BST, sub_tree: BST) -> bool:
        global flag
        global counter1
        global counter2
        if tree != None and sub_tree == None:
            counter1 += 1
            

        if tree == None and sub_tree != None:
            counter2 += 1
            

        if tree != None and sub_tree != None:
            counter1 += 1
            counter2 += 1
            print("tree: ", tree.key, "subtree: ", sub_tree.key)
            
                
            self.find_sub_tree(tree.left, sub_tree.left)
            self.find_sub_tree(tree.right, sub_tree.right)
        
        if counter1 != counter2:
            flag = False
        else:
            flag = True
            
            

def main() -> None:
    
    tree = BST(5)
    tree.insert(BST(3))
    tree.insert(BST(1))
    tree.insert(BST(4))
    tree.insert(BST(7))
    tree.insert(BST(3))
    tree.display()

    print("\n")

    sub_tree = BST(3)
    sub_tree.insert(BST(1))
    sub_tree.insert(BST(4))
    sub_tree.insert(BST(2))
    
    sub_tree.display()

    sol = Solution(tree, sub_tree)
    sol.find_sub_tree(sol.tree.left, sol.sub_tree)
    if flag:
        print("1_Given subtree is in original tree")
    else:
        sol.find_sub_tree(sol.tree.right, sol.sub_tree)
        if flag:
            print("2_Given subtree is in original tree")
        else:
            print("There is no such subtree in original tree.")
    print(flag)

if __name__ == "__main__":
    main()