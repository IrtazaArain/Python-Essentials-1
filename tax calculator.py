def tax_calculator(n):
    if n < 85528:
       tax = float(round((n *0.18)-556.2))
       if tax < 0:
          tax = 0.0
       print(f"The tax is: {tax} thalers")
        
    else:
        tax = float(round(((n - 85528) * 0.32) + 14839))
        print(f"The tax is: {tax} thalers")
n = float(input("Please enter your income: "))
tax_calculator(n)
