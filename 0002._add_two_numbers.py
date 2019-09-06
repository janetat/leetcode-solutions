# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # coner cases
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        list1 = []
        list2 = []

        # list -> str -> int -> sum
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        str1 = ''.join([str(i) for i in list1[::-1]])
        str2 = ''.join([str(i) for i in list2[::-1]])

        sum = str(int(str1) + int(str2))
        sum = sum[::-1]

        # build new linked_list with sum
        head = ListNode(int(sum[0]))
        cursor = head
        for i in range(1, len(sum)):
            cursor.next = ListNode(int(sum[i]))
            cursor = cursor.next

        return head


class Solution2:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        carry = 0
        dummy_head = cursor = ListNode(0)

        while l1 or l2 or carry:  # 链表l1, l2遍历完后，仍要考虑前一次求和是否有进位。
            num1 = num2 = 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next

            carry, val = divmod(num1 + num2 + carry, 10)
            cursor.next = ListNode(val)
            cursor = cursor.next

        return dummy_head.next


class Solution3:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            carry = 1
            l3 = ListNode(l1.val + l2.val - 10)
            l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(carry)))

        return l3
