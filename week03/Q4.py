#4
mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Charlie", "Frank"}

mondayClass.add("Grace")
print("Monday class", mondayClass)
print("wednesday class", wednesdayClass)
bothClass = mondayClass & wednesdayClass
print("Attended both class", bothClass)
allStudents = mondayClass | wednesdayClass
print("Attended either class", allStudents)
onlyOne = mondayClass ^ wednesdayClass
print("Only one class:", onlyOne)
print("is Monday subset of all students?", mondayClass <= allStudents)
