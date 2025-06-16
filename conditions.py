#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

#Based on a user's order, work out their final bill.

#Small Pizza: 20 Large Pizza: 2 Pepperoni for Medium or Large Pizza: +1

#Example Input

#size = "L" add_pepperoni = "Y" extra_cheese = "N"

#Example Output

#Your final bill is: $28.

#Hint

#Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.


def pizza(size,add_pepperoni,extra_cheese):
  small_pizza = 15
  medium_pizza = 20
  large_pizza = 25
  pepperoni = 3
  cheese = 1

  if size == "S":
    bill = small_pizza
  elif size == "M":
    bill = medium_pizza
  elif size == "L":
    bill = large_pizza
  else:
    print("Invalid size, enter S, M, L")
    return None

  if add_pepperoni == "Y":
    if size == "M" or size == "L":
      bill += pepperoni
    else:
      bill += 2

  if extra_cheese == "Y":
    bill += cheese

  print ("your bill is:", bill)
  return bill



#organization are entered through the keyboard. If the number of years for // which the employee has // # served the organization is greater than 3 then a bonus of Rs. 2500/- is // given to the employee. If the years of service are not greater // # than 3, then the program should do nothing.

def emp_bonus(years):
  if years > 3:
    bonus = 2500
    print(f"employee will get a bonus:", {bonus})
  else:
    print(f"employee is not eligible for a bonus")

years = int(input())
emp_bonus(years)




pizza("S", "Y", "N")







#The marks obtained by a student in 5 different subjects are input // through the keyboard. The student gets a // # division as per the following rules: Percentage above or equal to 60 - // First division // # Percentage between 50 and 59 - Second division // # Percentage between 40 and 49 - Third division // # Percentage less than 40 - Fail // # Write a program to calculate the division obtained by the student

def marks(a1,a2,a3,a4,a5):
  per = ((a1 + a2 + a3 + a4 + a5) / 500 ) * 100

  if per >= 60:
   divison = "first division"
  elif 50 <= per < 60:
   divison = "second division"
  elif 40 <= per < 49:
   divison = "third division"
  else:
   divison = "fail"

  print(f"student percentage is:", per)
  print(f"student division is:", divison)

a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())
a5=int(input())
marks(a1,a2,a3,a4,a5)

-----

def cal_div():
  marks = []
  for i in range(5):
    mark = int(input(f"enter the marks of subject {i + 1}: "))
    marks.append(mark)

  per = (sum(marks) / 500 ) * 100

  if per >= 60:
   divison = "first division"
  elif 50 <= per < 60:
   divison = "second division"
  elif 40 <= per < 49:
   divison = "third division"
  else:
   divison = "fail"

  print(f"student percentage is:", per)
  print(f"student division is:", divison)

cal_div()


