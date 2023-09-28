#Kitavi Duncan Gitau
#sct211-0031/2021


name = input("Enter Your Name: ")
print("Hello " +name)
num1 = input("Input a Number ")
num1 = int(num1)

operator = input("Input Operator either * ,+ ,- ,/ ,% ")

num2 = input("Input another number ")
num2 = int(num2)

if operator == "+":
    print(num1+num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
     print(num1*num2)

elif operator == "/":
     print(num1/num2)

elif operator == "%":
    print(num1%num2)

else:
    print("Inavlid Input")


