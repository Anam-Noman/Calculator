num1=int(input("Enter a number: "))
num2=int(input("Enter a another number: "))
print("Enter a operator (+,-,*,/) ")
opr=input("Enter a operator: ")

if  opr=="+":
    sum=num1+num2
    print(f"The answer is \"{sum}\"")
               
if  opr=="-":
    diff=num1-num2
    print(f"The answer is \"{diff}\"")
if  opr=="*":
    prod=num1*num2
    print(f"The answer is \"{prod}\"")
if  opr=="/":
    div=num1/num2
    print(f"The answer is \"{div}\"")


