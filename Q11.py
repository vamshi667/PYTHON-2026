subjects = ["Python", "SQL", "Excel", "Tableau"]

#11a. Display complete list
print("Complete List:", subjects)

#11b. Display first and last subject
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

#11c. Add one new subject between Python and SQL
subjects.insert(1, "Power BI")
print("Updated List:", subjects)

#11d. Delete Excel
subjects.remove("Excel")
print("After Removing Excel:", subjects)

#11e. Copy list into another list
new_list = subjects.copy()
print("Copied List:", new_list)

#11f. Sort the new list
new_list.sort()
print("Sorted List:", new_list)

#11g. Check if Excel is present
print("Is Excel Present?", "Excel" in subjects)
