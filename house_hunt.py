print("How long will it take me to buy a house?")
r = 0.04
current_savings = 0
number_of_months = 0
months_in_year = 12


annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")



total_cost = input("Enter the cost of your dream home: ")
portion_down_payment = int(total_cost) * float(0.25)
print("Your Down payment will be " + str(portion_down_payment) + ".")

# Repeat each month:

save_more = True
while save_more:
    monthly_savings = annual_salary // str(12) * str(portion_saved) 
    ann_return_month = current_savings * r / 12
    current_savings = monthly_savings + ann_return_month

    if current_savings >= portion_down_payment:
        save_more = False
    else:
        number_of_months = number_of_months + 1

print("Congrats! you saved " +str(current_savings) + "in just" + str(num_of_months) + "! enough for that " +str(portion_down_payment) + " down payment!")



# print("Number of months:")



