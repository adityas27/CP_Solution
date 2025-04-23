# a) Personalized Greeting Generator - Write a python code to generate Personalized Greeting.

name = input("Enter the name: ")
occasion = input("Enter the occasion (optional): ")
time_of_day = input("Enter the time of day (optional): ")
greeting = f"Good {time_of_day} {name}, Happy {occasion} !"
print(greeting)


# b)  Calculating Areas of Geometric Figures - Write a python program to calculate areas of any geometric figures like circle, rectangle and triangle.

# Circle Area Calculation 
radius = 0
area_circle = 0
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14159 * (radius ** 2)
print("Area of the circle is:",area_circle)

# Rectangle Area Calculation
length = 0
width = 0
area_rectangle = 0
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print("Area of the rectangle is:",area_rectangle)

# Triangle Area Calculation
base = 0
height = 0
area_triangle = 0
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print("Area of the triangle is:",area_triangle)