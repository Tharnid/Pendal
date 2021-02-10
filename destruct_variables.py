# x = 5 , 11 # tuple...brackets are not necessary...list with tuples inside 
             # you need the brackets

# destructured x until two variables
# t = 5,11
# x, y = t
# print(x, y)

student_attendance = {"Rolf": 96, "Bob": 88, "Anne": 100}

print(list(student_attendance.items())) # turns this in to a list

# for student, attendance in student_attendance.items():
#   print(f"{student}: {attendance}")

for student, attendance in student_attendance.items():
  #print(t)
  print(f"{student}: {attendance}")

people = [("Tharnid", 46, "Programmer"), ("Aragoth", 40, "Data Analyst"), ("Saldor", 46, "Database Admin"), ("Ebaq", 43, "SEO Engineer")]

for name, age, profession in people:
 print(f"Name: {name}, Age: {age}, Profession: {profession}") 