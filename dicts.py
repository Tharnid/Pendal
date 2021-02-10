# associate keys and values

# friend_ages = {"Rolf": 45, "Randy": 49, "Jason": 47, "Terrell": 48}

# friend_ages: dict
# print(friend_ages["Rolf"])

# friends = [
#   {"name": "Saldor", "age": 43},
#   {"name": "Ylix", "age": 51},
#   {"name": "Ebaq", "age": 46},
# ]

# print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 88, "Anne": 100}

# for student in student_attendance:
#   print(student)

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")
 
 # get just the values
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))