'''
    - Request an input from user and store the result as <principal>
    - Request an input from user and store the result as <annual_interest_rate>
    - Request an input from user and store the result as <loan_term_years>
    - Divide <annual_interest_rate> by 100 and divide the result by 12
    - Represents the result as <monthly_interest_rate>
    - Multiply loan_term_years by 12 and represent the result as <number_of_payments>
    - Multiply <principal> by <monthly_interest_rate> and <monthly_interest_rate> incremented by 1
    - Square the result and divide by <monthly_interest_rate> & incremented by 1 and subtract number_of_payments by 1
    - Represents the result as <monthly_payment> and display the result.
'''

principal = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
loan_term_years = int(input("Enter the loan term in years: "))

monthly_interest_rate = (annual_interest_rate / 100) / 12
number_of_payments = loan_term_years * 12

monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)

print(f"The monthly payment is NGN{monthly_payment:.2f}")
