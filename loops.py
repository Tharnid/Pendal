# while loop

# number = 7

# while True: # user_input != "n":
#   user_input = input("Would you like to play? (Y/n): ") 

#   if user_input == "n":
#     break

#   user_number = int(input("Guess our number: "))
#   if user_number == number:
#     print("You guessed correctly!!!")
#   elif abs(number - user_number) == 1: # abs absolute values
#     print("You were off by one.")
#   else:
#     print("Sorry, it's wrong!!!")
  

# print("Thanks for stopping by!!!")

# for loop

# friends = ["Terrell", "Saldor", "Jenny", "Tharnid"]

# for friend in friends:  # for friend in range(4)
#   print(f"{friend} is my friend!!!")

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

#for grade in grades:
  # total += grade # shorthand of total = total + grade

print(total / amount)