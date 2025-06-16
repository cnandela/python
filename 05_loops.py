#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line. Hints: Consider use range(#begin, #end) method
def find_numbers():
  result = []
  for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
      result.append(i)
  return result

numbers = find_numbers()
comma_separated_numbers = ", ".join(str(i) for i in numbers)
print(f"numbers are:", comma_separated_numbers)
