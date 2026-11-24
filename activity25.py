

def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x + 1):
            print("*", end=" ")
        print()

def multiply(x, y):
    return x + y

taga_triangle(10)
taga_triangle(8)
taga_triangle(7)

print(multiply(12, 3))
print(multiply(12, 3)* 5)

def box(size):
    for x in range(size + 1):
        for y in range(size + 1):
            if y == 0 or x == 0 or y == size or x == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
box(20)
box(30)

def my_factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

my_factorial(2)