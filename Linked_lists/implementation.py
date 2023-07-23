class linked_list_node:
    def __init__(self,data):
        self.data = data
        self.next = None


def linked_list_input():
    arr = [int(x) for x in input().split()]
    head = None
    for curr_data in arr:
        if curr_data == -1:
            break
        else:
            new_node = linked_list_node(curr_data)
            if head is None:
                head = new_node
                tail = head
            else:
                tail.next = new_node #type:ignore
                tail = tail.next     #type:ignore
    return head




def linked_list_print(head):
    while head is not None:
        print(head.data,end="-->")
        head = head.next
    print("None")


def linked_list_reverse_iterative(head):
    curr = head
    prev = None
    while curr is not None:
        save = curr.next
        curr.next = prev
        prev = curr
        curr = save
    return prev

def linked_list_reverse_recursion(head):
    if head.next is None:
        return head
    smallhead = linked_list_reverse_recursion(head.next)
    
    head.next.next = head
    head.next = None

    return smallhead

#driver

head = linked_list_input()
linked_list_print(head)
rev_head = linked_list_reverse_recursion(head)
linked_list_print(rev_head)
            
