print("\nQ10:")
student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course_name = input("Enter Course Name: ")

sub1 = float(input("Enter Marks in Subject 1: "))
sub2 = float(input("Enter Marks in Subject 2: "))
sub3 = float(input("Enter Marks in Subject 3: "))

total = sub1 + sub2 + sub3
percentage = total / 3

print("\nStudent Details")
print("Name:", student_name)
print("Age:", age)
print("City:", city)
print("Course:", course_name)
print("Percentage:", percentage)
