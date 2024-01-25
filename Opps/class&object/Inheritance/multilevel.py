'''it is a multi labeled inheritance'''
''' Bank class  --. hdfc_bank --> icici '''
class Bank :
    def transaction(slef) :
        print("total transaction value")

    def account_opening(self) :
        print("this will show the status of account opening")

    def deposit(self) :
        print("this will show deposited amount")

class hdfc_bank(Bank) :
    def hdfc_to_icici(self) :
        print('this will show all the transitions happend to icici through hdfc')

class icici(hdfc_bank) :
    pass

i = icici()
i.hdfc_to_icici()
i.deposit()
i.account_opening()
i.transaction()
        