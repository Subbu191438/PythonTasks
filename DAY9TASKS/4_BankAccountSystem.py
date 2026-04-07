class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account No:", self.acc_no)
        print("Balance:", self.balance)
acc1 = BankAccount(12345, 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.display()
