print ('===ATM Withdrawal Simulator===')
name = input('Enter Customer Name:')
balance = float(input('Enter Account balance:'))
Withdraw = float(input('Enter Withdrawal Amount:'))
if Withdraw<= 0:
    print('Invalid withdrawal amount')
elif Withdraw > balance:
    print('Insufficient funds.')
else:
    balance = balance - Withdraw
    print('\n===RECEIPT===')
    print('Customer:', name)
    print('Amount Withdrawn:', Withdraw)
    print('Remaining balance:', balance)