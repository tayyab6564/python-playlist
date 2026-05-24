#just like array in other programming languages.
# Lists are mutable, which means you can change their content without changing their identity.
#it can store different data types
list1=[11,4,2,66,7,21,9,0,1,5,3,8]
print(list1)
list2=["apple","banana","cherry"]
print(list2)    
list3=[1,"apple",3.14,True]
print(list3)
# accessing list items
print(list1[0]) #output: 1
print(list2[1]) #output: banana
print(list3[2]) #output: 3.14   

#               Modifying list items
list1[0]=10
print(list1) #output: [10, 4, 2, 66, 7, 21, 9, 0, 1, 5, 3, 8]  
list2[1]="grape"

#               List slicing
print(list1[1:4]) #output: [4, 2, 66]
    
#               List methods
list1.append(8) # adds 8 to the end of the list
print(list1) #output: [10, 4, 2, 66, 7, 21, 9, 0, 1, 5, 3, 8]

#              sorting a list

list2=["banana","apple","cherry"]
list2.sort() # sorts the list in ascending order
print(list2) #output: ['apple', 'banana', 'cherry']
list2.sort(reverse=True) # sorts the list in descending order
print(list2) #output: ['cherry', 'banana', 'apple']


list1.sort() # sorts the list in ascending order
print(list1) #output: [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 21, 66]
list1.sort(reverse=True) # sorts the list in descending order
print(list1) #output: [66, 21, 10, 9, 8, 7, 5, 4, 3, 2, 1, 0]


