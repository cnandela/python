#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Your program should work for different inputs. e.g. any two-digit number.

#Example Input 39 Example Output 3 + 9 = 12

#12

#Hint Try to find out the data type of two_digit_number. Think about what you learnt about subscripting.

def two_digit_sum(number):
   sub_str = str(number)
   first_digit = int(sub_str[0])
   second_digit = int(sub_str[1])

   sum = first_digit + second_digit
   return sum

number = input()
print("sum of two digits:", two_digit_sum(number))





#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

#The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

#Example Input

#weight = 80 height = 1.75

#Example Output

#80 ÷ (1.75 x 1.75) = 26.122448979591837

#26

def bmi(weight, height):
  bmi_c = weight / (height ** 2)
  return bmi_c

print("bmi is:", bmi(80,5))







#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

#https://waitbutwhy.com/2014/05/life-weeks.html

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.

#Where x, y and z are replaced with the actual calculated numbers.

#Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

#Example Input

#56

#Example Output

#You have 12410 days, 1768 weeks, and 408 months left.

#Hint

#There are 365 days in a year, 52 weeks in a year and 12 months in a year. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.


def age_left(age):
  max_age = 90
  age_left = max_age - age

  days_left = age_left * 365
  weeks_left = age_left * 52
  months_left = age_left * 12

  print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
  return days_left, weeks_left, months_left

age_left(50)
