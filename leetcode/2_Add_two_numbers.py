# Definition for singly-linked list.


def addTwoNumbers(
    l1, l2):

    perenos = 0
    result = ListNode()
    cursor = result

    # считаем первую ноду
    cursor.val = (l1.val + l2.val)


    while l1 or l2 or perenos:
        val1 = l1.val
        val2 = l2.val

        digit = (val1 + val2) % 10
        perenos = (val1 + val2) // 10

        cursor.val = digit

        cursor = cursor.next

    return result


if __name__ == '__main__':
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(addTwoNumbers(l1,l2))








# def addTwoNumbers(
#     l1):

#     res = str(l1.val)

#     while l1.next:
#         l1 = l1.next
#         res += str(l1.val)
    
#     return res

print(addTwoNumbers(l1))
print(addTwoNumbers(l2))

