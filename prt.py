principal=int(input("enter the principal amount:"))
rate=int(input("enter the interest rate:"))
time=int(input("enter time in years:"))
interest=(principal*rate*time)/100
totalamount=principal+interest
print("interest=",interest)
print("total amount=",totalamount)