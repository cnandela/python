#For a list ["foo", "bar", "baz"] add an item in the list "bar", what's the cleanest way to get its index (1) in Python?
my_list = ["foo", "bar", "baz"]
index_bar = my_list.index("bar")
print(index_bar)



#Best way to check if a list is empty

my_list = []

if not my_list:
  print("list is empty")
else:
  print("list is not empty")



#Getting the last element of a list in Python

my_list = ["abc", "def", "123", "453", "hdg"]
last_index = my_list[-1]
print(last_index)



#How to clone or copy a list?

my_list1 = ["abc", "134", "323", "ascc", "452"]
my_list2 = my_list1.copy()

print(my_list1)
print(my_list2)



#How can I count the occurrences of a list item in Python?

my_list = ["abc", "abc", "hgds", "123", "123", "222"]
occurence = my_list.count("abc")
print(occurence)




#How do I remove the first Item from a Python list?

my_list = ["abc", "def", "123", "544", "23", "fsa"]
print(f"before removing item: {my_list}")
x = my_list.pop(0)
print(f"removed item is: {x}")
print(f"after removing item: {my_list}")
