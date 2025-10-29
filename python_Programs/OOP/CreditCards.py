from BankDetails import BankDetails

class CreditCard(BankDetails):
    def __init__(self, custid, custname, Bal, creditscore, status):
        super().__init__(custid, custname, Bal)
        self.creditscore = creditscore
        self.status = status

    def wel_message(self):
        print(f'Welcome to Bank ,{self.custname}')

    def display_cc_details(self):
        print(f' {self.creditscore} - {self.status}')
