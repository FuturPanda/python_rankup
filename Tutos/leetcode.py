#  Two Sum

# def two_sum(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] + arr[j] == target and arr[i] != arr[j]:
#                 return [i, j]
#     return None

# def two_sum(arr, target):
#     seen = {}
#     for i, num in enumerate(arr):
#         if target-num in seen:
#             return ([seen[target-num], i])
#         else:
#             seen[num] = i


# arr_num = [2, 7, 11, 15]
# target = 14
# print(two_sum(arr_num, target))
# Expected = [0, 1]


# Linked List from scratch :
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, val=0, next=None) -> None:
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


first_list = LinkedList()
fl_one = Node("2")
# fl_two = Node(4)
# fl_three = Node(3)
first_list.head = fl_one
# fl_one.next = fl_two
# fl_two.next = fl_three
print(first_list)


# def addtwoNumbers(listnode1, listnode2) :
