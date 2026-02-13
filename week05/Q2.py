# Question 2: FizzBuzz

print("\n" + "=" * 50)
print("Question 2: FizzBuzz (#412)")
print("=" * 50)


def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result



print("\nTest Case 1: n = 3")
result = fizz_buzz(3)
print("Output: " + str(result))

print("\nTest Case 2: n = 5")
result = fizz_buzz(5)
print("Output: " + str(result))

print("\nTest Case 3: n = 15")
result = fizz_buzz(15)
print("Output: " + str(result))

print("\nTest Case 4: n = 1")
result = fizz_buzz(1)
print("Output: " + str(result))
