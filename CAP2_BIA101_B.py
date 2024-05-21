# Define tax brackets with income limits and corresponding tax rates in Bhutan
tax_brackets = [
    (300000, 0.0),     # No tax for income up to 300,000
    (400000, 0.1),     # 10% tax for income between 300,001 and 400,000
    (650000, 0.15),    # 15% tax for income between 400,001 and 650,000
    (1000000, 0.2),    # 20% tax for income between 650,001 and 1,000,000
    (1500000, 0.25),   # 25% tax for income between 1,000,001 and 1,500,000
    (float('inf'), 0.3) # 30% tax for income above 1,500,000
]

class Person:# Base class for a person with a name and method to calculate tax
    def __init__(self, name):
        self.name = name

    def calculate_tax(self, total_income):
        tax_payable = 0
        previous_limit = 0

        for limit, rate in tax_brackets:# Iterate over the tax brackets to calculate tax
            if total_income > limit:
                taxable_income = limit - previous_limit
                tax_payable += taxable_income * rate
                previous_limit = limit
            else:
                taxable_income = total_income - previous_limit
                tax_payable += taxable_income * rate
                break

        # Apply a surcharge if the tax payable exceeds 1,000,000
        if tax_payable >= 1000000:
            tax_payable *= 1.1

        return tax_payable

class Employee(Person):# Subclass for an employee with specific income and deductions
    def __init__(self, name, employment_income, pf_contribution, gis_contribution, education_allowance_per_child=0):
        super().__init__(name)
        self.employment_income = employment_income
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution
        self.education_allowance_per_child = education_allowance_per_child

    def calculate_income(self):# Calculate taxable income by deducting PF and GIS contributions from employment income
        taxable_income = self.employment_income - self.pf_contribution - self.gis_contribution
        return taxable_income

class Landlord(Person):# Subclass for a landlord with rental income and standard deductions
    def __init__(self, name, rental_income):
        super().__init__(name)
        self.rental_income = rental_income

    def calculate_income(self):# Calculate taxable rental income by deducting 20% of rental income
        deductions = self.rental_income * 0.2
        taxable_income = self.rental_income - deductions
        return taxable_income

class Investor(Person):# Subclass for an investor with dividend income and fixed deductions
    def __init__(self, name, dividend_income):
        super().__init__(name)
        self.dividend_income = dividend_income

    def calculate_income(self): # Calculate taxable dividend income by deducting a fixed amount
        taxable_income = max(0, self.dividend_income - 30000)
        return taxable_income

class Consultant(Person):# Subclass for a consultant with other income and standard deductions
    def __init__(self, name, other_income):
        super().__init__(name)
        self.other_income = other_income

    def calculate_income(self):# Calculate taxable consulting income by deducting 30% of other income
        deductions = self.other_income * 0.3
        taxable_income = self.other_income - deductions
        return taxable_income

# Create instances of each subclass with specific income values as an example
employee = Employee("John Doe", 500000, 50000, 10000, education_allowance_per_child=350000)
landlord = Landlord("Tom Brown", 400000)
investor = Investor("Alice Williams", 100000)
consultant = Consultant("Bob Johnson", 700000)

for person in [employee, landlord, investor, consultant]:# Iterate over each person, calculate their income and tax, and print the results
    income = person.calculate_income()
    tax = person.calculate_tax(income)
    print(f"{person.name}'s total income: Nu. {income:.2f}")
    print(f"{person.name}'s total tax payable: Nu. {tax:.2f}")
