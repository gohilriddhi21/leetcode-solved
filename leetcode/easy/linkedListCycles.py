class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if fast is head:
                return True
        return False

def print_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))


if __name__ == "__main__":
    s = Solution()
    # 1 -> 3 -> 5 -> 1 
    ll = ListNode(1, ListNode(3, ListNode(5)))
    ll.next.next.next = ll

    # 1
    ll2 = ListNode(1)
    print(s.hasCycle(ll2))