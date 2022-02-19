class Account():
    owner = ''
    balance = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        print(f'Name: {self.owner} \nBalance: {self.balance} ')
        return 0
    def deposit(self, money):
        self.balance += money
        print(f'{self.owner} your balance is: ', end = '')
        return self.balance
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f'{self.owner} your remaining balance is: ', end = '')
            return self.balance
        else:
            print(f'Not enough money \nBalance is: ')
            return self.balance
name = input('Enter the name of the owner: ')
balance = int(input('Enter the balance: '))
ac = Account(name, balance)
deposit = int(input('Enter the amount to deposit: '))
print(ac.deposit(deposit))
withdraw = int(input('Enter the amount to withdraw: '))
print(ac.withdraw(withdraw))