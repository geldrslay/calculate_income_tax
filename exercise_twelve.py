# Calculate income tax for the given income by adhering to the rules below
# First $10,000 has 0% rate
# Next $10,000 has a 10% rate
# The remaining amount has a 20% rate. 

# Display the given income. 
given_income = 45000
print ('The given income is: $', given_income)

# Determine income tax payable if income is less than or equal to $10,000. 
if given_income <= 10000:
    tax_payable = 0
# Determine income tax payable if income is less than or equal to $20,000
elif given_income <= 20000:
    income_with_tax= given_income - 10000
    tax_payable = income_with_tax * 10 / 100
# Determine income tax payable if income is greater than $20,000
else: 
    tax_payable = 0
    tax_payable = 10000 * 10 /100
    tax_payable += (given_income-20000) * 20 / 100

# Display the total income tax payable 
print ("If income is $",given_income,"then the total income tax payable is $",tax_payable)
