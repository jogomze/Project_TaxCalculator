# Income Tax Calculator
# This project study develops a program that calculates income tax. Each year, nearly everyone with an income faces the unpleasant task of computing his or her income tax return. If only it could be done as easily as suggested here! We start with the customer request phase.

# Request
# The customer requests a program that computes a person’s income tax.

# Analysis
# Analysis often requires the programmer to learn some things about the problem domain, in this case, the relevant tax law. For the sake of simplicity, let’s assume the following tax laws:

# All taxpayers are charged a flat tax rate of 20%
# All taxpayers are allowed a $10,000 standard deduction
# For each dependent, a taxpayer is allowed an additional $3,000 deduction
# Gross income must be entered to the nearest penny
# The income tax is expressed as a decimal number
# Another part of analysis determines what information the user will have to provide. In this case, the user inputs are gross income and number of dependents. The program calculates the income tax based on the inputs and the tax law and then displays the income tax. The figure below shows the proposed terminal-based interface. Characters in italics indicate user inputs. The program prints the rest. The inclusion of an interface at this point is a good idea because it allows the customer and the programmer to discuss the intended program’s behavior in a context understand- able to both.


# Constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Inputs
gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

# Calculate taxable income
taxable_income = gross_income - STANDARD_DEDUCTION - (num_dependents * DEPENDENT_DEDUCTION)

# Calculate income tax
income_tax = taxable_income * TAX_RATE

# Display income tax
print("The income tax is: $", format(income_tax, ".1f"), sep="")
