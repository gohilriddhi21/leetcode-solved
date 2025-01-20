class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 or list2
    return dummy.next


def print_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))


if __name__ == "__main__":
    # 1 -> 3 -> 5
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    
    # 1 -> 2 -> 4
    l2 = ListNode(1, ListNode(2, ListNode(4)))

    merged_head = mergeTwoLists(l1, l2)
    print_list(merged_head)
