# Question 3: Shuffle the Array

def shuffle_array(nums, n):
    first_half = nums[:n]
    second_half = nums[n:]

    result = []

    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result
