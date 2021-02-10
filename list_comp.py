numbers = [1,3,5]
doubled = [num * 2 for num in numbers]

# for num in numbers:
#   doubled.append(num * 2)

friends =["Tharnid", "Saldor", "Terrell", "Aragoth"]
starts_t = [friend for friend in friends if friend.startswith("T")]

# for friend in friends:
#   if friend.startswith("T"):
#     starts_t.append(friend)

print(starts_t)