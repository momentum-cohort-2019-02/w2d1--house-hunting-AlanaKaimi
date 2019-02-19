# How long will it take to save enough for Down Payment on House?

# Get annual salary
annual_salary = float(input("Enter your annual salary: $"))
# Get % of monthly salary to be saved
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# Get cost of dream home
total_cost = float(input("Enter the cost of your dream home: "))
# Calculate Down payment
portion_down_payment = total_cost * 0.25

# Define variables
current_savings = 0
r = 0.04
number_of_months = 0

# Each month
while current_savings <= portion_down_payment:
    # add month
    number_of_months += 1
    # calculate new current savings
    current_savings += (annual_salary/12)*portion_saved + current_savings*(r/12)

# return answer
print("Number of Months ", number_of_months)



