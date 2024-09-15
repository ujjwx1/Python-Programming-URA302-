print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")

first_name = input("First name: ")
last_name = input("Last name: ")
print(last_name, first_name)

import math
radius = float(input("Radius: "))
print(math.pi * radius ** 2)

colors = ["Red", "Green", "White", "Black"]
print(colors[0], colors[-1])

n = input("Number: ")
print(int(n) + int(n*2) + int(n*3))

nums = input("Comma-separated numbers: ").split(",")
print(nums, tuple(nums))

c = float(input("Celsius: "))
print(c * 9/5 + 32)

a, b = int(input("First number: ")), int(input("Second number: "))
a, b = b, a + 1
print(a, b)

num = int(input("Number: "))
print("Even" if num % 2 == 0 else "Odd")

year = int(input("Year: "))
print("Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year")

x1, y1 = map(float, input("x1 y1: ").split())
x2, y2 = map(float, input("x2 y2: ").split())
print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

a1, a2, a3 = float(input()), float(input()), float(input())
print("Triangle" if a1 + a2 + a3 == 180 else "Not a triangle")

P, r, t, n = float(input()), float(input()), float(input()), float(input())
A = P * (1 + r / (100 * n)) ** (n * t)
print(A - P)

n = int(input())
print("Prime" if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)) else "Not prime")

N = int(input())
print(sum(i**2 for i in range(1, N+1)))
