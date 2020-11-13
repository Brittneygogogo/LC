'''
递归
'''


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def isPalindrome(self, head) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


root = ListNode(5)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(5)

x = Solution()
print(x.isPalindrome(root))

'''
反转后半部分链表
这题是让判断链表是否是回文链表，所谓的回文链表就是以链表中间为中心点两边对称。
我们常见的有判断一个字符串是否是回文字符串，这个比较简单，可以使用两个指针，一个最左边一个最右边，两个指针同时往中间靠，判断所指的字符是否相等。

但这题判断的是链表，因为这里是单向链表，只能从前往后访问，不能从后往前访问，所以使用判断字符串的那种方式是行不通的。
但我们可以通过找到链表的中间节点然后把链表后半部分反转（关于链表的反转可以看下432，剑指 Offer-反转链表的3种方式），最后再用后半部分反转的链表和前半部分一个个比较即可。

public boolean isPalindrome(ListNode head) {
    ListNode fast = head, slow = head;
    //通过快慢指针找到中点
    while (fast != null && fast.next != null) {
        fast = fast.next.next;
        slow = slow.next;
    }
    //如果fast不为空，说明链表的长度是奇数个
    if (fast != null) {
        slow = slow.next;
    }
    //反转后半部分链表
    slow = reverse(slow);

    fast = head;
    while (slow != null) {
        //然后比较，判断节点值是否相等
        if (fast.val != slow.val)
            return false;
        fast = fast.next;
        slow = slow.next;
    }
    return true;
}

//反转链表
public ListNode reverse(ListNode head) {
    ListNode prev = null;
    while (head != null) {
        ListNode next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

'''
