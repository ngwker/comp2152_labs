# Question 3: Binary Search

print("\n" + "=" * 50)
print("Question 3: Binary Search (#704)")
print("=" * 50)



def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Recursive
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)

    return binary_search_recursive(nums, target, mid + 1, right)


def search_recursive(nums, target):
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)



test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 3),
    ([], 5),
]

for nums, target in test_cases:
    result = binary_search_iterative(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))

for nums, target in test_cases:
    result = search_recursive(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))