num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print(f"Addition=,{num1+num2:.2f}")
print(f"Multiplication=,{num1*num2:.2f}")
if num2!=0:
    print(f"Division=,{num1/num2:.2f}")
    print(f"Floor Division=,{num1//num2:.2f}")
    print(f"Modulus=,{num1%num2:.2f}")
else:
    print("Division, floor division and modulus are undefined for zero divisor.")
print(f"Exponentiation=,{num1**num2:.2f}")