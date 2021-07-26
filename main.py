# Exercise 2 - Faulty calculator
#45*3=555,56+9=77,56/6=4
#Design a calaculator which will correctly solve all the problems except the following ones:
#45*3=555,56+9=77,56/6=4
#Your progress should take operator and the two numbers a sinput from the user and then return the result
print("Welcome to The Saacket's faulty Calculator")
print("Enter first number")
num1=int(input())
print("Enter Second number")
num2=int(input())
print("Enter your Operator")
op=input()
if op=='+'and num1==54 and num2==5 :
    print("64")
elif op=='*'and num1==45 and num2==3 :
    print("555")
elif op == '/' and num1 == 56 and num2 == 6:
    print("4")


elif op == '+':
   print(num1+num2)
elif op == '-':
   print(num1-num2)
elif op == '*':
   print(num1*num2)
elif op == '/':
   print(num1/num2)
else:
    print("Invalid Input")

