def calculate_future_investment(amount, rate, years):
    number_of_months = years * 12
    monthly_rate = rate / 12
    return amount * (1 + monthly_rate) ** number_of_months