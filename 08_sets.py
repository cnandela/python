#Remove duplicate values of a list a=[1,2,3,4,1,2,3,10]

a = [1,2,3,4,1,2,3,10]
a_set = set(a)
a_list = list(a_set)

print(f"list is:", a_list)
