#LoanCalculator

# define the loan calculator function

def calculate_loan(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100

# the amount of payments
    amt_payments = years * 12

# the monthly payment using the formula for a fixed-rate loan. This is the formula to pay off a loan over a certain perioud of time
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** amt_payments) / ((1 + monthly_interest_rate) ** amt_payments - 1)

# total payment 
    total_payment = monthly_payment * amt_payments

# total interest
    total_interest = total_payment - principal
    return total_payment, total_interest, monthly_payment

# define the main function to interact with the user
# next: setup above variables to ask for user for input 
# get user input for loan details

# call the the loan calculator function