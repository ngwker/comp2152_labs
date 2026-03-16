# Question 2 shopping cart list - searching - and removal
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples", cart.count("apple"))
print("position of milk", cart.index("milk"))
cart.remove("apple")
print("Remove item using pop", cart.pop())
print("is banana in the cart?", "banana" in cart)
print("final cart", cart)

point1=(3,5)
point2=(37,2)
print(f"Point 1: {point1}\nPoint 2: {point2}\n")
x1, y1 = point1
x2, y2 = point2
print(f"x1{x1}, y1\nx2: {x2}, y2: {y2}\n")
distance = ((x2-x1)**2 + (y2-y1)**2)** 0.5
print("Distance between points:", distance)

