class Bank:
    def __init__(self, name, no, bal):
        self.name = name
        self.no = no
        self.bal = bal
    
    def deposite(self, dep):
        self.dep = dep
        self.balance = self.balance + self.dep

    def withd(self, amt):
        self.amt = amt
        if self.bal > self.amt:
            self.bal - self.amt
        else:
            print("insuff balance")

        
