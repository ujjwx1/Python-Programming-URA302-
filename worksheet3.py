def calculate_difference(number):
    

    difference = number - 17
    if number > 17:
        difference *= 2
    return difference


result = calculate_difference(20)
print(result)



def is_within_range(number):
    

    return (100 <= number <= 1000) or (number == 2000)


result = is_within_range(500)
print(result) 





def reverse_string(string):
   

    return string[::-1]


result = reverse_string("hello")
print(result)  




def count_letters(string):
    
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


result = count_letters("Hello, World!")
print(result) 




def remove_duplicates(lst):
    

    return list(set(lst))


result = remove_duplicates([1, 2, 3, 2, 4, 1])
print(result)  





def print_even_numbers(lst):
    
    for num in lst:
        if num % 2 == 0:
            print(num)


print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])




def outer_function():
    def inner_function():
        print("This is the inner function.")

    inner_function()


outer_function()




def student(name, age, grade):
    

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")


student("Alice", 18, "10th")







class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")


student1 = Student(123, "John Doe")
student1.student_class = "10th"
student1.display_attributes()



class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(123, "Alice")
student2 = Student(456, "Bob")

print(f"Student 1: ID={student1.student_id}, Name={student1.student_name}")
print(f"Student 2: ID={student2.student_id}, Name={student2.student_name}")




import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print(f"Area: {circle.calculate_area()}")
print(f"Perimeter: {circle.calculate_perimeter()}")




class StringProcessor:
    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())


processor = StringProcessor()
processor.get_string()
processor.print_string()