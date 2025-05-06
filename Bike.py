
price=int(input("Enter price of bike: "))
tax=0

if price>80000:
    tax=(15*price)/100
    print("15% tax is:", tax)
elif (price > 40000 and price<80000): 
       tax=(10*price)/100
       print("10% tax is:", tax)
else:  
       tax=(5*price)/100
       print("5% tax is:", tax)