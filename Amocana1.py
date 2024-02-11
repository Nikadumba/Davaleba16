

class BankAccount:
    

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def inflow(self, inflow_amount):
        print(f"Account Number: {self.account_number}, Client Name: {self.account_holder}, Current Balance: {self.balance}")
        self.balance += inflow_amount
        print(f"{self.account_holder} - Balance after inflow: {self.balance} \n")

    def outflow(self, outflow_amount):
        print(f"Account Number: {self.account_number}, Client Name: {self.account_holder}, Current Balance: {self.balance}")
        if self.balance < outflow_amount:
            print(f"{self.account_holder} - Insufficient balance ({self.balance}) \n")
        else:
            self.balance -= outflow_amount
            print(f"{self.account_holder} - Balance after outflow: {self.balance} \n")

client1 = BankAccount("GE00BG1111222233334444", "Nikoloz Dumbadze", 1000)
client1.inflow(100)
client1.outflow(200)
client1.inflow(500)
client1.outflow(2000)
client1.outflow(100)

client2 = BankAccount("GE11TB0000111122223333", "Giorgi Giorgadze", 500)
client2.outflow(200)
client2.inflow(400)
