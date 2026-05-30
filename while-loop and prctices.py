# print hello 6 times using while loop
"""
count = 0
while count < 6:
    print("hello")
    count += 1
    """

    # print table of a number using while loop
"""
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

    # print all values of a list using while loop

    num = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(num):
    print(num[i])
    i += 1
                        """

# search for a specific value in a list using while loop
"""
num1 = (1,4,9,16,25,36,49,81,64,81,100)  
search = int(input("Enter a number to search: ") ) 
i = 0
count = 0
while i < len(num1):
   if (num1[i]==search) :
      print("Number found at index ",i)
      i+=1
      count+=1
   else :
      i+=1
"""
              # break and continue in loop
#"continue" runs a piece of code next to it if condition became false           
#Example: print odd numbers from 1 to 10
"""
print("odd: ")
j=0
while j<=10:
    if(j%2 == 0):
        j+=1
        continue
    print(j)
    j+=1

# print even numbers fom 1 to 10
print("even: ")
j=0
while j<=10:
    if(j%2 != 0):
        j+=1
        continue
    print(j)
    j+=1
"""
# break is used to terminate program on a specific condition
i = 0
while i < 20:
    print(i)
    if i == 7:
        break
    i += 1
   