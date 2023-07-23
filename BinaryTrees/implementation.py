import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def binary_tree_input_normal():
    root_data = int(input())
    if root_data == -1:
        return
    root = BinaryTreeNode(root_data)

    root.left = binary_tree_input_normal() # type: ignore
    root.right = binary_tree_input_normal() # type: ignore

    return root

def binary_tree_input_levelwise():
    q = queue.Queue()
    root_data = int(input("Enter Root "))
    if root_data ==-1:
        return
    root = BinaryTreeNode(root_data)
    q.put(root)

    while q.empty() == False:
        front = q.get()

        print(f"Enter Left Child of {front.data}")
        lc_data = int(input())
        if lc_data != -1:
            lc = BinaryTreeNode(lc_data)
            front.left = lc
            q.put(lc)

        print(f"Enter Right Child of {front.data}")
        rc_data = int(input())
        if rc_data != -1:
            rc = BinaryTreeNode(rc_data)
            front.right = rc
            q.put(rc)
    return root  






def binary_tree_print_inorder(root):
    if root is None:
        return
    
    binary_tree_print_inorder(root.left)
    print(root.data,end=" ")
    binary_tree_print_inorder(root.right)

def binary_tree_print_preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    binary_tree_print_preorder(root.left)
    binary_tree_print_preorder(root.right)

def binary_tree_print_postorder(root):
    if root is None:
        return
    
    binary_tree_print_postorder(root.left)
    binary_tree_print_postorder(root.right)
    print(root.data,end=" ")

def binary_tree_print_levelwise(root):
    q = queue.Queue()
    q.put(root)
    q.put(None)

    while not q.empty():
        front = q.get()
        if front is not None:
            print(front.data,end=" ")

            if front.left:
                q.put(front.left)
            if front.right:
                q.put(front.right)
        else:
            if q.empty()==True:
                break
            else:
                q.put(None)
                print()






# Driver

root = binary_tree_input_levelwise()

binary_tree_print_levelwise(root)
# binary_tree_print_postorder(root)
# binary_tree_print_preorder(root)