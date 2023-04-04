from structure import LinkedList, ListNode

# lst = [1, 2, 3, 4, 5] # => false
# lst = [1, 2, 3, 2, 1] # => true
lst = [1, 2, 2, 1]

ll = LinkedList()
for i in lst:
    ll.append(i)

# class Solution:
#     def is_palindrome(self, head) -> bool:
#         arr = []
#         node = head.head
#         while node:
#             arr.append(node.val)
#             node = node.next
#         print(arr)
#         return True


def is_palindrome(ll) -> bool:
    arr = []
    node = ll.head
    while node:
        arr.append(node.val)
        node = node.next
    while len(arr) > 1:
        if arr.pop(0) != arr.pop():
            return False
    return True


print(is_palindrome(ll))

ll.remove(2)

ll.print()