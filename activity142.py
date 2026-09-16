age = int(input("What is your age -->"))
is_employed = bool(input("Are you currently employed? -->"))
credit_score = int(input("Enter your credit score -->"))
annual_income = float(input("What is your annual income? -->"))
has_collateral = bool(input("Do you have collateral?"))

base_rate = 0.0
#outer condition

if age >= 21 and is_employed == True:
    print("Congratulations! You are eligible for loan")
    if credit_score >=750:
        print("You have high credit score")
        if annual_income >=100000:
            base_rate = 4.5
            print("You have high credit score and annual income, your interest rate is", base_rate)
        else:
            base_rate = 5.0
            print("You have high credit score and annual income, your interest rate is", base_rate)
    elif 600 <= credit_score < 750:
            if has_collateral == True:
                base_rate = 7.0
                print("You have high credit score and annual income, your interest rate is", base_rate)
            elif annual_income < 40000:
                base_rate = 9.5
                print("You have fair credit score and low annual income, your interest rate is", base_rate)
            else:
                base_rate = 8.0
                print("You have fair credit score and low annual income, your interest rate is", base_rate)
                if credit_score < 600:
                    print("Credit score is too low, you are not eligible for loan")
    else:
        print("Failed")
else:
    print("Rejected: Fails baseline criteria")

