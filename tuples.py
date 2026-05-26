#tuples are also similar to lists, but they are immutable which means you cannot change their content after they are created.
tup = ()
tup1 = (1,)  #<-- tup1 = (1) will be considered as an integer, not a tuple. To create a tuple with a single element, you need to include a comma after the element.
tup2 = (1, 2, 3, 4, 5)
tup3 = ("apple", "banana", "cherry")
print(tup) #output: ()
print(tup1) #output: (1,)       
print(tup2) #output: (1, 2, 3, 4, 5)
print(tup3) #output: ('apple', 'banana', 'cherry')

# changes not allowed in tuples
#tup2[0] = 10 <----this will raise a TypeError: 'tuple' object does not support item assignment

#              accessing tuple items

print(tup2[0]) #output: 1   
print(tup3[1]) #output: banana

#             tuple slicing
print(tup2[1:4]) #output: (2, 3, 4)
print(tup3[0:2]) #output: ('apple', 'banana')

#             concatenation of tuples
tup4 = tup2 + tup3
print(tup4) #output: (1, 2, 3, 4, 5, 'apple', 'banana', 'cherry')

#             repetition of tuples
tup5 = tup1 * 3
print(tup5) #output: (1, 1, 1)
 
tup6 = tup3 * 2
print(tup6) #output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#             unpacking of tuples
a, b, c, d, e = tup2    
print(a) #output: 1
print(b) #output: 2
print(c) #output: 3
print(d) #output: 4
print(e) #output: 5

#           nested tuples
tup7 = (1, 2, (3, 4), 5)
print(tup7) #output: (1, 2, (3, 4), 5)
print(tup7[2]) #output: (3, 4)
print(tup7[2][0]) #output: 3
print(tup7[2][1]) #output: 4

#             tuple methods
print(tup2.count(1)) #output: 1
print(tup2.index(3)) #output: 2  (index of first occurrence of 3 in tup2)
