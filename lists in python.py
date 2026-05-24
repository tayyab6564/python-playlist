#just like array in other programming languages.
# Lists are mutable, which means you can change their content without changing their identity.
#it can store different data types
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
list2=["apple","banana","cherry"]
print(list2)    
list3=[1,"apple",3.14,True]
print(list3)
# accessing list items
print(list1[0]) #output: 1
print(list2[1]) #output: banana
print(list3[2]) #output: 3.14   

# Modifying list items
list1[0]=10
print(list1) #output: [10, 2, 3, 4, 5]  
list2[1]="grape"

# List slicing
print(list1[1:4]) #output: [2, 3, 4]

# List methods
list1.append(6)
print(list1) #output: [10, 2, 3, 4, 5, 6]