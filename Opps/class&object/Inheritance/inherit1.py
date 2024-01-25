class Bank :
    def transaction(slef) :
        print("total transaction value")

    def account_opening(self) :
        print("this will show the status of account opening")

    def deposit(self) :
        print("this will show deposited amount")
    
    def test(self) :
         print("this is a test method from bank")
    

class hdfc_bank :
    def hdfc_to_icici(self) :
        print('this will show all the transitions happend to icici through hdfc')

    def test(self) :
         print("this is a test method from hdfc bank")

class ineuron_bank :
     def account_status_icici(self) :
          print("account status")

class icici(Bank,hdfc_bank,ineuron_bank) :
            pass

i  = icici()
i.account_opening()
i.deposit()
i.hdfc_to_icici()
i.transaction()
i.test()  # it will give test function from bank because in icici class we passed bank class first in child class.
i.account_status_icici()