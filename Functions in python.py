# Functions are used to enhance re-useability and redundancy of code

def sum(a , b):
    return a + b
addition = sum(4 , 5)
print("Result of sum is : " , addition)

#Function call :

addition = sum(5 , 6)
print("Result of sum is : " , addition)
addition = sum(2 , 1)
print("Result of sum is : " , addition)
addition = sum(598 , 67)
print("Result of sum is : " , addition)
addition = sum(7001 , 2)
print("Result of sum is : " , addition)

#print hello world
def hello():
  print("Hello world")
hello()  

#Average of values
def average(a , b , c):
   return (a+b+c)/3
print(average(4 , 6 , 2))