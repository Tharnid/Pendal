# in keyword

friends = ["Terrell", "Tharnid", "Jenny"]
print("Jenny" in friends)

movies_watched = {"The Matrix", "Oceans 12", "1907"}
user_movie = input("Enter something you've watched recently: ").lower()

print(user_movie in movies_watched)

# if with in keyword

movies_watched = {"The Matrix", "Oceans 12", "1907"}
user_movie = input("Enter something you've watched recently: ")

# print(user_movie in movies_watched)
if user_movie in movies_watched:
  print(f"I've watched {user_movie} too!!!")
else:
  print("I haven't watched that yet")