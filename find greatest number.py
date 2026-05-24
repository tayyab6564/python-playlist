num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
if(num1>num2 and num1>num3):
    print(num1," is greatest among all numbers")
elif(num2>num1 and num2>num3):
        print(num2," is greatest amoung all")
elif(num3>num1 and num3>num2):
    print(num3," is greatest among all")
elif(num1==num2 and num1==num3):
    print("all numbers are equal")
elif(num1==num2 and num1>num3):
    print(num1," and ",num2," are greatest among all")
elif(num1==num3 and num1>num2):
    print(num1," and ",num3," are greatest among all")
else:
    print(num2," and ",num3," are greatest among all")          
