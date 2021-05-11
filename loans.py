#Conditions: highincome and good credit = eligable for loan
has_high_income = True
has_good_credit = False
crim_record = True

#Need both to be true
#Bank 1
if has_high_income and has_good_credit:
    print("BANK 1:Eligable for Loan")
else: print("BANK 2:Not Eligable for Loan")

#ONLY ONE NEED TRUE
#Bank 2
if has_high_income or has_good_credit:
    print("BANK 2: Eligable for Loan 1/2")
else:
    print("BANK 2: You don't qualify")

#Bank 3
if has_good_credit and not crim_record:
    print("Bank 3: Eligable for Loan")
else: print("Bank 3: You are not Eligable For Loan")