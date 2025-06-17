#Remove duplicate values of a list a=[1,2,3,4,1,2,3,10]

a = [1,2,3,4,1,2,3,10]
a_set = set(a)
a_list = list(a_set)

print(f"list is:", a_list)




#Remove duplicate values of a list a=[1,2,3,4,1,2,3,10]

#What is the output when the following code is run by Python? For sets, do not worry about getting the exact order of the output correct. s1 = set( [7,9, 12, 7, 9] ) s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ]) s3 = set( [12, 14, 12, 'ab'] )

#print s1 & s2

#print s1 | s2

#print 'b' in s2

#print 'ab' in s2

#print 'ab' in s3

#s2.discard(12)

#print (s1 & s2) ^ s3

s1 = set( [7,9, 12, 7, 9] )
s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
s3 = set( [12, 14, 12, 'ab'] )

print(s1)
print(s2)
print(s3)
print(s1 & s2)
print(s1 | s2)
print('b' in s2)
print('ab' in s2)
print('ab' in s3)
s2.discard(12)
print(s2)
print((s1 & s2) ^ s3)
