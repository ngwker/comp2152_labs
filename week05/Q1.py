# Question 1: Fibonacci Number
print("\n" + "=" * 50)
print("Question 1: Fibonacci Number (#509)")
print("=" * 50)


def fib(n):


    if n == 0:
        return 0


    if n == 1:
        return 1


    return fib(n-1) + fib(n-2)



print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    result = fib(i)
    print("F(" + str(i) + ") = " + str(result))

print("\nAdditional test cases:")
print("F(15) = " + str(fib(15)))
print("F(20) = " + str(fib(20)))
