def function1(price):
    price=price-(price*10/100)
    return price
def function2(newprice):
    newprice=newprice-(newprice*5/100)
    return newprice
org_price = int(input("enter the original price"))
print("price after discount:",function2(function1(org_price)))
