class Payment:
    def process_payment(self):
        print("Processing payment...")

class CreditCard(Payment):
    def process_payment(self):
        print("Payment done using Credit Card")

class UPI(Payment):
    def process_payment(self):
        print("Payment done using UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Payment done using Net Banking")
payments = [CreditCard(), UPI(), NetBanking()]

for p in payments:
    p.process_payment()
