amt = float(input('enter your bill cost:'))
per = float(input('enteer the percentage you want to tip:'))

def waiter_tip(amt,per):
    tip = amt*(per/100)
    tbill = amt + tip
    print(tbill,tip)

waiter_tip(amt,per)