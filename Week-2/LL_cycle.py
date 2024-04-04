class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head is None:
        return False
    
    while head.next:
        if head.val is None:
            return True
        head.val = None
        head = head.next 
    
    return False

