# Question 2: Two Sum



def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None



def two_sum_optimized(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed], i)

        seen[numbers[i]] = i

    return None
