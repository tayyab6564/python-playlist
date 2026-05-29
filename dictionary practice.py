#store table and cat as keys and their definitions as values in a dictionary

dictionary = {
"table": ["a piece of furniture","list of facts and figures"],
"cat": "a small animal"
}
print(dictionary) 

# here are some subjects given for each subject we need a separate class
# calculate how many classrooms are rquired to read all subjects
# subjects = "java", "python", "c++", "python", "javascript", "java", "c++", "python", "javascript", "java"

subjects = {"java", "python", "c++", "python", "javascript", "java", "c++", "python", "javascript", "java"}
print(len(subjects)) #output: 4 (there are 4 unique subjects)

# start with an empty dictionary and add subject as a key and numbers as a value to it
classrooms = {}
classrooms["java"] = int(input("Enter marks for java: "))
classrooms["python"] = int(input("Enter marks for python: "))
classrooms["c++"] = int(input("Enter marks for c++: "))
classrooms["javascript"] = int(input("Enter marks for javascript: "))
print(classrooms)

# store 9 and 9.0 as a separate value in the dictionary 
numbers = {
9 , "9.0"
}
print(numbers)