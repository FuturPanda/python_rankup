# 1 - Binary Search Algorithm.
def binarySearch(nums, target):

    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)

    # loop till the search space is exhausted
    while left <= right:

        # find the mid-value in the search space and
        # compares it with the target

        mid = (left + right) // 2

        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2

        # target is found
        if target == nums[mid]:
            return mid

        # discard all elements in the right search space,
        # including the middle element
        elif target < nums[mid]:
            right = mid - 1

        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1

    # `target` doesn't exist in the list
    return -1


def my_search_algo(nums, target):
    left, right = 0, (len(nums)-1)
    while left <= right:
        print("searching")
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid-1
        else:
            left = mid + 1
    return -1


print(my_search_algo([2, 5, 6, 8, 9, 10, 67, 138, 244, 512], 139))


# if __name__ == '__main__':

#     nums = [2, 5, 6, 8, 9, 10]
#     target = 5

#     index = my_search_algo(nums, target)

#     if index != -1:
#         print('Element found at index', index)
#     else:
#         print('Element found not in the list')
