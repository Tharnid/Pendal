# for loop

# friends = ["Terrell", "Saldor", "Jenny", "Tharnid"]

# for friend in friends:  # for friend in range(4)
#   print(f"{friend} is my friend!!!")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
  total += grade # shorthand of total = total + grade

print(total / amount)