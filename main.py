# l = ["Terrell", "Tharnid", "Babydoll"] # list []...
# t = ("Terrell", "Tharnid", "Babydoll") # tuple ()...can't modify
# s = {"Terrell", "Tharnid", "Babydoll"} # set {}...no duplicates..order does not stay the same

# lists and tuples keep order

# print(l[0]) # subscript notation
# l.append("Jenny")
# print(l)
# l.append("Jenny")
# print(l)
# # l.remove("Jenny")
# print(l)

# s.add("Jenny")
# print(s)

# day_of_week = input("What day of the week is it today? ")

# if day_of_week == "Monday":
#    print("Have a great start to your week!!!")

# if day_of_week != "Monday":
#   print("Enjoy your day!!!")

# print("This prints no matter what")

# day_of_week = input("What day of the week is it today? ").lower()

# if day_of_week == "monday":
#    print("Have a great start to your week!!!")

# elif day_of_week == "tuesday":
#   print("It's only Tuesday!!!")

# else:
#   print("Enjoy your day!!!")

# print("This prints no matter what")

# in keyword

# friends = ["Terrell", "Tharnid", "Jenny"]
# print("Jenny" in friends)

# in

# movies_watched = {"The Matrix", "Oceans 12", "1907"}
# user_movie = input("Enter something you've watched recently: ")

# print(user_movie in movies_watched)

# if in

# movies_watched = {"The Matrix", "Oceans 12", "1907"}
# user_movie = input("Enter something you've watched recently: ")

# print(user_movie in movies_watched)
# if user_movie in movies_watched:
#   print(f"I've watched {user_movie} too!!!")
# else:
#   print("I haven't watched that yet")

# Magic Number
number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
  user_number = int(input("Guess our number: "))
  if user_number == number:
    print("You guessed correctly!!!")
  elif abs(number - user_number) == 1: # abs absolute values
    print("You were off by one.")
  else:
    print("Sorry, it's wrong!!!")

else:
  print("Thanks for stopping by!!!")