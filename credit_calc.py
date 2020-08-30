# Program that is used to  calculate  annuity payment ,principal, count of periods, and the value of payment.
# The user specifies all the known parameters using command-line arguments, so there will be one unknown parameter.
# Program work from the command line and parse the following parameters:
# --type, which indicates the type of payment: "annuity" or "diff" (differentiated).
# --payment, which refers to the monthly payment. For --type=diff, the payment is different each month, so we cannot calculate a number of periods or the principal
# --principal is used for calculating both types of payment. You can get its value knowing the interest, the annuity payment, and the number of periods.
# --periods parameter denotes the number of months and / or years needed to repay the credit.It 's calculated based on the interest, annuity payment, and the principal.
#--interest
# Example 1: calculating differentiated payments
# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Example 2: finding the annuity payment for the 60-month (or 5-year) credit loan with the principal 1,000,000 and a 10% interest
# > python
# creditcalc.py - -type = annuity - -principal = 1000000 - -periods = 60 - -interest = 10
# Example 3: calculating differentiated payments given the principal 500,000, the period of 8 months, and an interest rate of 7.8%
# > python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# Example 4: calculating the principal for an individual paying 8,722 per month for 120 months (10 years) with an interest rate of 5.6%
# > python
# creditcalc.py - -type = annuity - -payment = 8722 - -periods = 120 - -interest = 5.6
# Example 7: figuring out how much time an individual needs to repay the credit loan with the principal 500,000, the monthly payment of 23,000 at a 7.8% interest rate
# > python
# creditcalc.py - -type = annuity - -principal = 500000 - -payment = 23000 - -interest = 7.8



import sys,math

import argparse

parser = argparse.ArgumentParser(description='credit calculator')
parser.add_argument("--type",required=True,help="type of payment annuity or differentiate")
parser.add_argument("--payment",type=int,help="monthly payment")
parser.add_argument("--principal",type=int,help="principal_credit")
parser.add_argument("--interest",type=float,required=True,help="stopa procentowa kredytu")
parser.add_argument("--periods",type=int,help="periods of payment")

args=parser.parse_args()
# print(args)
# print(len(sys.argv))
# print(args.interest)

def diff_payment():
    i = args.interest / (12 * 100)
    x = 1
    suma = 0
    while x <= args.periods:
        monthly_payment = math.ceil(args.principal / args.periods + i * (args.principal - (args.principal * (x - 1) / args.periods)))
        print(f"Month {x}: paid out {monthly_payment}")
        x += 1
        suma += monthly_payment
    print()
    print(f"Overpayment = {suma - args.principal}")

def annuity_payment():
    i= args.interest / (12 * 100)
    #print(i)
    if args.payment==None:
        monthly_payment = math.ceil(args.principal * ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1)))
        print(f"Your annuity payment = {monthly_payment}!")
        suma=monthly_payment*args.periods
        print(f"Overpayment = {math.ceil(suma-args.principal)}")
    elif args.principal==None:
        credit_principal = math.floor(args.payment * (((1 + i)**args.periods - 1) / (i * (1 + i)**args.periods)))
        print(f"Your credit principal = {(credit_principal)}!")
        suma = args.payment * args.periods
        print(f"Overpayment = {math.ceil(suma - credit_principal)}")
    elif args.periods==None:
        count_of_period = math.ceil(math.log(args.payment, 1 + i) - math.log(args.payment - i * args.principal, 1 + i))
        if count_of_period % 12==0:
            print(f"You need {int(count_of_period/12)} years to repay this credit!")
        else:
            print(f"You need {count_of_period // 12} years and {count_of_period % 12} months to repay this credit!")
        suma=args.payment*count_of_period
        print(f"Overpayment = {math.ceil(suma - args.principal)}")

def negative_parameters():
    if args.principal==None:
        if args.periods<0 or args.payment<0 or args.interest<0:
            return "Incorrect parameters"
        else:
            return None
    if args.periods==None:
        if args.principal<0 or args.payment<0 or args.interest<0:
            return "Incorrect parameters"
        else:
            return None
    if args.payment==None:
        if args.principal<0 or args.periods<0 or args.interest<0:
            return "Incorrect parameters"
        else:
            return None


    # if args.interest==None:
    #     if args.periods<0 or args.payment<0 or args.interest<0:
    #         print("Incorrect parameters")


def credit_calc():
    # if args.periods<0 or args.principal<0 or args.interest<0 or args.payment<0:
    #     print("Incorrect parameters")
    negatives = negative_parameters()
    #print(negatives)
    if args.interest==None:
         print("incorrect parameters")

    elif negatives:
         print(negatives)
    elif len(sys.argv)==9:
        if args.type == "diff":
            if args.payment==None:

                diff_payment()
            else:
                print("Incorrect parameters")
        elif args.type == "annuity":

            annuity_payment()
        else:
            print("Incorect parameters")
    else:
        print("Incorrect parameters")

credit_calc()








