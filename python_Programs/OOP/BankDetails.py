from typing import final


class BankDetails:
    def __init__(self, custid, custname, Bal):
        self.custid = custid
        self.custname = custname
        self.Bal = Bal
    
    def wel_message(self):
        print("Welcome to Bank Details")

    def display_details(self):
        print(f' {self.custid} - {self.custname} - {self.Bal}')


