age = int(input("Age: "))
rev = float(input("REVENUE: "))
cc = int(input("CREDIT SCORE: "))
yrs = float(input("YEARS OF BUSINES: "))
has_defaults = bool(input("FILE FOR BANKRUPT: "))
collateral = input("COLLATERAL NAME:" )
c_value = float(input("COLLATERAL VALUE: "))

max_loan = 0
base_fee = 0
#BASELINE CALC
if age >= 21 and yrs >=2.0 and has_defaults == False:
    print("APPLICATION APPROVED")
    #rules
    if c_value >= max_loan:
        print("Collateral", collateral, "with a value of", c_value)
    else:
        print("Insufficient value for", collateral)
        surge_fee_rate = max_loan * base_fee
    if max_loan % 5000 != 0:
        print("Additional Surge Fee Added")
        surge_fee_rate += 250
        print("Updated base fee is", base_fee)
    if cc >= 720:
        max_loan = 3*rev
        print("accepted")
        if rev >= 50000:
            print("Revenue is greater than 50000")
            base_fee = max_loan * 0.015
            print("Your base fee is", base_fee)
        else:
            base_fee = max_loan * 0.025
            print("Your base fee is", base_fee)
        if c_value >= max_loan:
            print("Collateral", collateral, "with a value of", c_value)
        else:
            print("Insufficient value for", collateral)
            surge_fee_rate = max_loan * base_fee
        if max_loan % 5000 != 0:
            print("Additional Surge Fee Added")
            surge_fee_rate += 250
            print("Updated base fee is", base_fee)

    elif cc >= 620 and cc < 720:
        max_loan = 1.5*rev
        print("Credit Score accepted according to range")
        if yrs >= 5.0:
            print("Business is more than 5 years")
            base_fee = max_loan * 0.02
            print("Base fee is", base_fee)
        else:
            print("Business is less than 5 years")
            base_fee = max_loan * 0.035
            print("Base fee is", base_fee)
        if c_value >= max_loan:
            print("Collateral", collateral, "with a value of", c_value)
        else:
            print("Insufficient value for", collateral)
        surge_fee_rate = max_loan * base_fee
        if max_loan % 5000 != 0:
            print("Additional Surge Fee Added")
            surge_fee_rate += 250
            print("Updated base fee is", base_fee)
    else:
        print("rejected")
else:
    print("APPLICATION REJECTED")
    