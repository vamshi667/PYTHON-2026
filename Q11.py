subjects = ["Python", "SQL", "Excel", "Tableau"]

# a. Display complete list
print("Complete List:", subjects)

# b. Display first and last subject
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# c. Add one new subject between Python and SQL
subjects.insert(1, "Power BI")
print("Updated List:", subjects)

# d. Delete Excel
subjects.remove("Excel")
print("After Removing Excel:", subjects)

# e. Copy list into another list
new_list = subjects.copy()
print("Copied List:", new_list)

# f. Sort the new list
new_list.sort()
print("Sorted List:", new_list)

# g. Check if Excel is present
print("Is Excel Present?", "Excel" in subjects)
