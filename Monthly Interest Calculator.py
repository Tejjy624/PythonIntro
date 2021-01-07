# Tejvir Sohi
# ECS32A Fall 2018
#
# monthly interest calculator
from inputCheck import canBeFloat
from inputCheck import canBeInt


def Judge(monthlyPayment, InterestRate, debtAmount):
    if canBeFloat (monthlyPayment) == False:
        print("Bad input, enter a number next time.")
        return False
    if canBeFloat (InterestRate) == False:
        print("Bad input, enter a number next time.")
        return False
    if canBeFloat (debtAmount) == False:
        print("Bad input, enter a number next time.")
        return False
    return True

debtAmount = input("Enter amount of debt:")
InterestRate = input("Enter % interest rate:")
monthlyPayment = input("Enter monthly payment:")

if(Judge(monthlyPayment, InterestRate, debtAmount)):
    debtAmount = float(debtAmount)
    InterestRate = float(InterestRate)
    monthlyPayment = float(monthlyPayment)
    month = 0
    monthlyInterest = InterestRate/12/100
    if(monthlyPayment <= debtAmount * InterestRate / 100):
        print("You will need to make bigger payments.\nAt this rate you will never pay off the debt.")
    else:
        while month < 4:
            month = month + 1
            print("Month = "+str(month))
            Interest = float(debtAmount) * float(monthlyInterest)
            debtAmount = debtAmount - monthlyPayment + Interest
            total = monthlyPayment*month
            if monthlyPayment > (debtAmount + monthlyPayment):
                total = monthlyPayment*month + debtAmount
            if debtAmount < 0:
                debtAmount = 0
            print("Interest this month = "+str("{:.2f}".format(Interest)))
            print("Balance going forward = "+str("{:.2f}".format(debtAmount)))
            print("Total payments = "+str("{:.2f}".format(total)))
input("Press enter to exit")
    
