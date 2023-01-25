x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())

if x == x_1 or x == x_2:
    if y_1 < y < y_2:
        print("Border")

if y == y_1 or y == y_2:
    if x_1 < x < x_2:
        print("Border")

else:
    print("Inside / Outside")



