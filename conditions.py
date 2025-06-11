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

pizza("S", "Y", "N")
