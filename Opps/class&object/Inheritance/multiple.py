class Bank :
    def transaction(slef) :
        print("total transaction value")

    def account_opening(self) :
        print("this will show the status of account opening")

    def deposit(self) :
        print("this will show deposited amount")
    
    

class hdfc_bank :
    def hdfc_to_icici(self) :
        print('this will show all the transitions happend to icici through hdfc')


class icici(Bank,hdfc_bank) :
            pass

i  = icici()
i.account_opening()
i.deposit()
i.hdfc_to_icici()
i.transaction()
i.test()