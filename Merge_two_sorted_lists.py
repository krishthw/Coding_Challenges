# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1:ListNode, list2:ListNode) -> ListNode:
    # if any of list is null return the other
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # set the head to least value from l1 and list2
    if list1.val < list2.val:
        temp = head =  ListNode(list1.val)
        list1 = list1.next
    else:
        temp = head = ListNode(list2.val)
        list2 = list2.next
        
    # loop until two lists become null
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            temp.next = ListNode(list1.val)
            list1 = list1.next
        else:
            temp.next = ListNode(list2.val)
            list2 = list2.next
        temp = temp.next
    # add if there are more in l1
    while list1 is not None:
        temp.next = ListNode(list1.val)
        list1 = list1.next
        temp = temp.next
    # add if there are more in l2

    while list2 is not None:
        temp.next = ListNode(list2.val)
        list2 = list2.next
        temp = temp.next

    return(head)