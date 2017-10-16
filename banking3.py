from banking import Account
from banking2 import Customer

names = []
firstname = input("please input the firstname")
lastname = input("please input the lastname")
account = input("please input the account")
customer = Customer(firstname, lastname)
namelist = (firstname, lastname)
names.append(namelist)

while True:
    print("choose one of these options\n"
          "1.Get Customer\t"
          "2.Get number of customer\n"
          "3.Add customer\t"
          "4.Deposit\n"
          "5.Withdraw\t"
          "6.Check Balance\n"
          "7.Set Account\t"
          "8.Get Account\n"
          "9.quit\n")

    ans = input("do you want to input another Customer y/n ?")
    if ans == 'y':
        firstname = input("please input the firstname")
        lastname = input("please input the lastname")
        account = input("please input the account")
        names.append(namelist)
    else:
        break
    money = 0
    balance = int(money)
    Balance = Account(balance)
    while True:
        j = int(input("how much do you want withdraw?"))
        Balance.withdraw(j)
        if Balance.getBalance(balance) < 0:
            print("not enough money")
            Balance.deposit(j)
            continue
        else:
            print(Balance.getBalance(balance), "$")

        break

    while True:
        j = input("")
        if j == "1":
            print(customer.account())
            break
        if j == "2":
            print(len(names))
            break
        if j == "3":
            firstname = input("please input the firstname")
            lastname = input("please input the lastname")
            account = input("please input the account")
            names.append(customer.customer(firstname + lastname + account))
            break
        if j == "4":
            j = int(input("how much do you want to deposit?"))
            Balance.deposit(j)
            print(Balance.getBalance(balance), "$")
            break
        if j == "5":
            print(Balance.getBalance(balance), "$")
            break

        if j == "6":
            print(Balance.getBalance(balance), "$")
            break
        if j == "7":
            account = input("please input the account")
            customer.setAccount(account)
            break
        if j == "8":
            print(customer.getAccount(account))
            break
        if j == "9":
            print("Thank You")
            break
        else:
            print("error")
            break
