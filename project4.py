def accountInput() -> int:
  numberString = input("Enter account number: ")
  if (numberString != "-1") & (numberString.isdigit() == False):
    raise "Account number should be a positive integer, zero or -1."
  return int(numberString)

def beginningBalanceInput() -> int:
  numberString = input("Enter beginning balance: ")
  if numberString.isdigit() == False:
    raise "Beginning balance should be a positive integer or zero."
  return int(numberString)

def totalChargeInput() -> int:
  numberString = input("Enter total charges: ")
  if numberString.isdigit() == False:
    raise "Total charges should be a positive integer or zero."
  return int(numberString)

def totalCreditInput() -> int:
  numberString = input("Enter total credits: ")
  if numberString.isdigit() == False:
    raise "Total credits should be a positive integer or zero."
  return int(numberString)

def creditLimitInput() -> int:
  numberString = input("Enter credit limit: ")
  if numberString.isdigit() == False:
    raise "Credit limit should be a positive integer or zero."
  return int(numberString)

def start():
  account = accountInput()

  if account == -1:
    return

  beginningBalance = beginningBalanceInput()
  totalCharge = totalChargeInput()
  totalCredit = totalCreditInput()
  creditLimit = creditLimitInput()
  newBalance = beginningBalance + totalCharge - totalCredit

  if newBalance <= creditLimit:
    print("")
    return start()
  
  print("")
  print(f'Account number is {account}')
  print(f'Credit limit is {creditLimit}')
  print(f'Balance is {newBalance}')
  print(f'Credit limit exceeded')
  print("")
  return start()

start()