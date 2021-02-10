# friends =["Tharnid", "Saldor", "Terrell", "Aragoth"]
# starts_t = []

# for friend in friends:
#   if friend.startswith("T"):
#     starts_t.append(friend)

# friends =["Tharnid", "Saldor", "Terrell", "Aragoth"]
# starts_t = [friend for friend in friends if friend.startswith("T")]

# print(starts_t)

# dicts
# friend_ages = {"Rolf": 45, "Randy": 49, "Jason": 47, "Terrell": 48}

# friend_ages["Rolf"] = 35
# print(friend_ages)

# friends = [
#   {"name": "Saldor", "age": 43},
#   {"name": "Ylix", "age": 51},
#   {"name": "Ebaq", "age": 46},
# ]

# print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 88, "Anne": 100}

# for student, attendance in student_attendance.items():
#   print(f"{student}: {attendance}")

# for student in student_attendance:
#   print(f"{student}: {student_attendance[student]}")
  # print(student)

# You can only check if keys are in the dictionary
# if "Bob" in student_attendance:
#   print(f"Bob: {student_attendance['Bob']}")
# else:
#   print("Bob is not a student!!!")

# get just the values
# attendance_values = student_attendance.values()
# print(sum(attendance_values) / len(attendance_values))

# student_attendance = {"Rolf": 96, "Bob": 88, "Anne": 100}

# print(list(student_attendance.items())) # turns this in to a list

# for student, attendance in student_attendance.items():
#   print(f"{student}: {attendance}")

# for student, attendance in student_attendance.items():
#   #print(t)
#   print(f"{student}: {attendance}")
# people = [("Tharnid", 46, "Programmer"), ("Aragoth", 40, "Data Analyst"), ("Saldor", 46, "Database Admin"), ("Ebaq", 43, "SEO Engineer")]

# for name, age, profession in people:
#  print(f"Name: {name}, Age: {age}, Profession: {profession}") 

# single tuple

# person = ("Bob", 42, "Mechanic")
# name, _, profession = person 

# print(name, profession)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail) 