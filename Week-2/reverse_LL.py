class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):    
    if head:
        last_node = ListNode(head.val)
        ans = last_node
    else:
        return None
    
    while head.next is not None:
        head = head.next
        ans = ListNode(val=head.val, next=last_node)
        last_node = ans 
    return ans


        
