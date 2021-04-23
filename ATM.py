import time
t = time.asctime()


name = input ('What is your name? \n')
allowedUser = 'Arinze'
pin = 1234

    
print (name, 'Kindly input your ATM pin')
ATMpin = int (input())
if (ATMpin == pin):
    print ('Welcome', name, '\n' 'The current date and time is', t)
    print ('1. Withdrawal')
    print ('2. Deposit')
    print ('3. Complaints')

    choosenOption = int(input('Please choose an option \n'))

    if(choosenOption == 1):
        print(int(input('How much would you like to withdraw \n')))
        print("Please take your cash")

    elif(choosenOption == 2):
        print(int(input('How much would you like to deposit \n')))
        print("Your current balance is")
       
    elif(choosenOption == 3):
        print(input('What issue will you like to report? \n'))
        print("Thank you for contacting us")

    else:
        print('Invalid option selected, kindly try again')

else:
    print('Name not found, please try again')
    

