#My Example
goodcredit = False


if goodcredit:
    print("The House cost is 1M$, So Your deposit is 100k")
else:
    print("Your credit is bad, so you need to put down 200k deposit")


#Tutorial Example
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")