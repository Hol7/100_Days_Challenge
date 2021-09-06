# If statement

print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))

if height == 190:
  print("you can ride the rollercoaster!")
else:
  print("sorry you can't")



# in this program we will try to kwon if year that user will enter is a leap year or a normal year 

year = int(input("which is the year do you want to check"))

if year % 4 == 0:
  if year % 100 == 0:
    print("It's a leap year")
    if year % 400 == 0:
      print("It's a leap year")
    else:
      print("Its not a leap year")
  else:
    print("It's not a leap year")
else:
  print("Its not leap year")
  
