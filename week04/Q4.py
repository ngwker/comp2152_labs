# Question 4: First Unique Character


def count_characters(s):
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def first_unique_character(s):
    char_counts = count_characters(s)

    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1