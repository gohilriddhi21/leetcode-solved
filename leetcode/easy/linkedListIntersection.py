class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 1
        l1 , l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1.val

def print_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))


if __name__ == "__main__":
    s = Solution()
    
    # 4 -> 1 -> 8 -> 4 -> 5
    ll1 = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    print_list(ll1)
    
    # 5 -> 6 -> 1 -> 8 -> 4 -> 5
    ll2 = ListNode(5, ListNode(6, ListNode(1, ll1.next.next))) 
    print_list(ll2)
    
    print(s.getIntersectionNode(ll1, ll2))
    
    # 4 -> 1 -> 8 -> 5
    ll1 = ListNode(4, ListNode(1, ListNode(8, ListNode(5))))
    print_list(ll1)
    
    # 5 -> 6 -> 1 -> 4 -> 8 -> 5
    ll2 = ListNode(5, ListNode(6, ListNode(1, ListNode(4, ll1.next.next)))) 
    print_list(ll2)
    
    print(s.getIntersectionNode(ll1, ll2))