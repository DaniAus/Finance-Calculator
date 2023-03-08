import math

print("""investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan \n""")
user_question = input ("Enter either 'investment' or 'bond' from the menu to proceed: ")
user_question = user_question.lower()
# Saving the answer to the question as lowercase to ensure however its spelt the code will run

if user_question == 'bond' or user_question == 'investment':
    ()
else:
    print("Please ensure you have entered either 'bond' or 'investment'")
# If the user doesnt enter bond or investment this message is shown

# Investment
if user_question == 'investment':
    money_deposit = float(input("How much money are you depositing? "))
    interest_rate = float(input("What is the interest rate as a percentage? "))
    invest_years = int(input("How many years do you plan on investing for? "))
    interest = input("Would you like 'simple' or 'compound' interest? ")
    interest = interest.lower()
# Asking the user how much money they are saving, percentage rate, years of investment and if they want simple or compund interest
# Also storing the answer to interest as lowercase to ensure the code contiunes to work no matter how they spell it

    interest_percentage = (interest_rate / 100)
    simple_for = money_deposit * (1 + interest_percentage * invest_years)
    compound_for = money_deposit * math.pow((1 + interest_percentage), invest_years)

    if interest == 'simple':
        print(f"Over {invest_years} years you will save £{simple_for:.2f}")
    elif interest == 'compound':
        print(f"Over {invest_years} years you will save £{compound_for:.2f}")
# Calculating the formulas for simple and compound interest 
# Displaying how much money the user will save over how many years

# Bond
if user_question == 'bond':
    house_value = float(input("What is the present value of the house? "))
    interest_rate2 = float(input("What is the interest rate? "))
    months = float(input("How many months are you planning to repay the bond? "))

    interest_rate2_percentage = ((interest_rate2 / 100) / 12)
    bond_for = (interest_rate2_percentage * house_value) / (1 - (1 + interest_rate2_percentage) ** (-months))

    print(f"You will have to repay £{bond_for:.2f} a month")
# Asking the user the value of the house, the interest rate and how many months they want to repay the bond over
# Using the formula to calculate the bonds
# Displaying how much money the user will have to pay a month