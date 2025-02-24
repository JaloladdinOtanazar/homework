def invest(amount, rate, years):
    principal = amount
    for year in range(1, years+1):
        principal += principal * rate
        print(f"year {year}: ${principal:.2f}")

amount = float(input("Enter the principal: "))
rate = float(input("Enter the annual rate of return: ")) 
years = int(input("Enter the number of years: "))
invest(amount, rate, years)