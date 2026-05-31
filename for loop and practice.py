# for loop can travers a list or tuple sequentially without using index
"""
num = [1,2,3,4,5,6]
for val in num :
    print(val)
"""

# search for a number using for loop

"""
    search = (23,22,1,54,76,88,12,55)  
    numb = int(input("enter a number to search: "))
    ind = 0
    for val in search :
        if val == numb : 
        print("value found at index ", ind)
        break
        ind += 1
                          """

    # Range function starts from 0 index and end will be specified
    #  3 ways to write Range function
    #                     1. Range(end)
    #                     2. Range(start , end)
    #                     3. Range(start , end , )
"""    
print("Range(ending value): ")
for i in range(10):
       print(i)

print("Range(starting , Ending):")  
for i in range(2 , 7):
       print(i)
       
print("Range(starting , Ending , step/increment):")  
for i in range(2 , 10 , 2):
       print(i)    

# Pass statment is used as placeholder for future code
for i in range(10):
      pass
"""
#practice 1:
#print sum of first 10 natural numbers
sum = 0
for i in range(1 , 11 ):
      sum+=i

print("total sum = ",sum)  

#print factorial of n natural numbers

val = int(input("Enter value to print factorial: "))
fac = 1
for i in range(val , 0 , -1):
      fac *= i

print(fac)      
