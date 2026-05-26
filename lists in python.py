#just like array in other programming languages.
# Lists are mutable, which means you can change their content without changing their identity.
#it can store different data types
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
list2=["apple","banana","cherry"]
print(list2)    
list3=[1,"apple",3.14,True]
print(list3)

#           accessing list items
print(list1[0]) #output: 1
print(list2[1]) #output: banana
print(list3[2]) #output: 3.14   

#         Modifying list items
list1[0]=10
print(list1) #output: [10, 2, 3, 4, 5]  
list2[1]="grape"
print(list2) #output: ['apple', 'grape', 'cherry']
list3[2]=3.14159
print(list3) #output: [1, 'apple', 3.14159, True]

#              List slicing
print(list1[1:4]) #output: [2, 3, 4]

#              insert an element at the end of the list
list1.append(6)
print(list1) #output: [10, 2, 3, 4, 5, 6]

#            insert an element
list2.insert(1,"orange") #inserts "orange" at index 1
print(list2) #output: ['apple', 'orange', 'grape', 'cherry']

#            remove any element
list4 = [1,3,6,5,32,0,1,9,7,8] 
list4.remove(1) #removes the first occurrence of 1 from the list
print(list4) #output: [3, 6, 5, 32, 0, 1, 9, 7, 8]
 
#             pop an element
list4.pop() #removes the last element from the list
print(list4) #output: [3, 6, 5, 32, 0, 1, 9, 7]

#             clear the list
list2.clear() #removes all elements from the list
print(list2) #output: []    

#             reverse the list
list4.reverse() #reverses the order of the list
print(list4) #output: [6, 5, 4, 3, 2, 10]

# 