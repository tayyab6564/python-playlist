#set is a collection of unique items, it is unordered and mutable
# Elements of sets are immutable, which means you cannot change the value of an element once it is added to the set, but you can add or remove elements from the set itself.

set1 = {1,2,3,4,5} #creating a set of numbers
print(set1) #output: {1, 2, 3, 4, 5}

fruit_set = {"apple", "banana", "cherry"} #creating a set of fruit names
print(fruit_set) #output: {'banana', 'cherry', 'apple'}

mixed_set = {1, "apple", 3.14, True} #creating a set of mixed data types
print(mixed_set) #output: {1, 3.14, 'apple', True}

# we cannot access set items by index because sets are unordered collections    

#            adding an element to the set
set1.add(6)
print(set1) #output: {1, 2, 3, 4, 5, 6}

#            removing an element from the set
fruit_set.remove("apple") #removes "apple" from the set, if "apple" is not present in the set it will raise a KeyError
print(fruit_set) #output: {'banana', 'cherry'}

#            discarding an element from the set
fruit_set.discard("banana") #removes "banana" from the set, if "banana" is not present in the set it will do nothing
print(fruit_set) #output: {'cherry'}


# two same elements cannot be added to the set, if we try to add a duplicate element it will be ignored
set1.add(3) #trying to add a duplicate element to the set   
set1.add(3) #trying to add a duplicate element to the set again
print(set1) #output: {1, 2, 3, 4, 5, 6} (the duplicate element "3" is ignored and not added to the set)

#               set operations
set2 = {4,5,6,7,8}  
print(set1.union(set2)) #output: {1, 2, 3, 4, 5, 6, 7, 8} (returns a new set that contains all unique elements from both sets)
print(set1.intersection(set2)) #output: {4, 5, 6} (returns a new set that contains only the elements that are present in both sets)
print(set1.difference(set2)) #output: {1, 2, 3} (returns a new set that contains only the elements that are present in the first set but not in the second set)
print(set1.symmetric_difference(set2)) #output: {1, 2, 3, 7, 8} (returns a new set that contains only the elements that are present in either of the sets but not in both sets)

#               set methods
print(set1.copy()) #output: {1, 2, 3, 4, 5, 6} (returns a shallow copy of the set)
print(set1.pop()) #output: 1 (removes and returns an random element from the set, since sets are unordered, we cannot predict which element will be removed)
print(set1) #output: {2, 3, 4, 5, 6} (the element "1" is removed from the set)
set1.clear() #removes all elements from the set
print(set1) #output: set() (the set is now empty)