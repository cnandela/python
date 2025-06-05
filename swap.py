# How to swap 2 variables( apart from , and +/- operator) in python
# Swap using multiplication and division 

a = 5 
b = 10 

a = a * b 
b = a // b 
a = a // b 

print("a =", a) 
print("b =", b)
