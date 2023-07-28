# mortgage.py
#
# Exercise 1.7

# principal = 500000
# rate = 0.05
# monthly = 2684.11
# paid = 0
# time = 0

# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000

def calc(principal, rate, monthly, extra_payment=0,\
            extra_payment_start_month=0, extra_payment_end_month=0):
    ''' wrapper for mortgage calc'''
    paid = 0
    time = 0

    while principal > 0:
        time += 1
        principal = principal * (1+rate/12) - monthly
        paid = paid + monthly
        # 1.19 extra payment
        if (time >= extra_payment_start_month) and (time <= extra_payment_end_month):
            principal -= extra_payment
            paid += extra_payment
        # 1.11 bonus code
        if principal < 0:
            paid += principal
            principal = 0
        # 1.10 table printing
        print(f'{time}\t{paid:0.2f}\t{principal:0.2f}')

# calc(500000,0.05,2684.11, extra_payment=1000,\
#             extra_payment_start_month=0, extra_payment_end_month=12)

calc(500000,0.05,2684.11, extra_payment=1000,\
            extra_payment_start_month=61, extra_payment_end_month=108)
