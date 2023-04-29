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
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __repr__(self):
#         return self.data


# class LinkedList:
#     def __init__(self, val=0, next=None) -> None:
#         self.head = None

#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return "->".join(nodes)


# first_list = LinkedList()
# fl_one = Node("2")
# # fl_two = Node(4)
# # fl_three = Node(3)
# first_list.head = fl_one
# # fl_one.next = fl_two
# # fl_two.next = fl_three
# print(first_list)


# def addtwoNumbers(listnode1, listnode2) :

# def lengthOfLongestSubstring(s):
#     char = {}
#     current_length = 0
#     max_length = 0
#     for i in enumerate(s):
#         if i[1] not in char:
#             char[i[1]] = i[0]
#             current_length += 1
#         elif i[1] in char:
#             max_length = current_length if current_length > max_length else max_length
#             if char[i[1]] < i[0] and char[i[1]] >= (i[0]-current_length):
#                 current_length = i[0] - char[i[1]]
#             else:
#                 current_length += 1
#             char[i[1]] = i[0]
#     max_length = current_length if current_length > max_length else max_length
#     return max_length

# print(lengthOfLongestSubstring("abcabcbb"))
# ----- Best Practice :
# def bp(s) :
#         st = 0
#         m = 0
#         d ={}
#         for i , v in enumerate(s):
#             if v in d and st <= d[v]:
#                 st = d[v]+1
#             else:
#                 m= max(m, i-st+1)
#             d[v] = i

#         return m


# ----- ----- ----- ----- ----- ---- ----- ----- -----
# def longestPalindrome(self, s):
#     sub = {}
#     cur_index_start = 0
#     index_mirror = None
#     cur_length = 0
#     longest = 0
#     res = ""
#     for i, letter in enumerate(s) :
#         if letter in sub :
#           if index_mirror == None :
#             index_mirror = i-1
#           if sub[letter]


# s = "babad"

# longestPalindrome(s)


# def check_pal(str):
#     return (str == str[::-1])


# Depth First search :

def numIslands(grid):
    if not grid:
        return 0
    col, row = len(grid[0]), len(grid)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
numIslands(grid)
