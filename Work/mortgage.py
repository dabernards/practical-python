# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05
monthly = 2684.11
paid = 0
time = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    time += 1
    if (time >= extra_payment_start_month) and (time <= extra_payment_end_month):
        if principal < monthly + extra_payment:
            paid = paid + principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - monthly - extra_payment
            paid = paid + monthly+ extra_payment
    else:
        if principal < monthly:
            paid = paid + principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - monthly
            paid = paid + monthly

    print(f'{time}\t{paid:0.2f}\t{principal:0.2f}')

