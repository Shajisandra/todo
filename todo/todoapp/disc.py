def function1(price):
    return price-(price*10/100)
def function2(price):
    return price-(price*5/100)
def discount(price):
    stud_price=function1(price)
    final_price=function2(stud_price)
    return final_price
price=int(input("enter the orginal price"))
final_price=discount(price)
print(final_price)