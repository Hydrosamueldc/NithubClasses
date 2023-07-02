students = {
    "Samuel":["Adegboyega", "Samuel", "male"],
    "john": ["john", "Doe", "male", "200 level"],
    "Adeola":["Adeola", "Awoyale", "female", "100 level"],
    "Qudus":["adelaja", "Qudus","male", "100 level"],
    "total_number": 3
}

print(students)
print(type(students))
print(students["Samuel"])
print(students.get("mary", "mary is not a student of the class"))
print(students.get("Adeola"))
print(students["Samuel"][2])
print("hydrosamuel" in students)

students["Samuel"]=["Adegboyega", "Aremu", "male", "100 level"]
print(students)

students.update({"Samuel":["Adegboyega", "Oladimeji", "male", "100 level"]})
print(students)
students.update({"total_number": 4})
print("\n\n")
print(students)

print("\n\n")
#upade an element in a list 
students["Qudus"]= students["Qudus"].append(1)
print(students)

