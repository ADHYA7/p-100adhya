class Atm:
    def _int_(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
    
    def checkBalance(self):
        print("YOUR BALANCE IS 50000")

    def withDraw(self,amount):
        newAmount=50000-amount
        print("YOU HAVE WITHDRAW"+str(amount)+'.your remaining balnace is '+str(newAmount))

def main():
        cardn=input("ENTER YOUR CARD NO.: ")
        pinN=input("ENTER YOUR PIN NO.: ")

        newUser = Atm(cardn,pinN)
        print ('choose your activity')
        print("1.checkBalance   2.withdraw")
        activity=int(input("enter the activity no.="))
        if activity==1:
            newUser.checkBalance()

        elif activity==2:
            amount=int(input('ENTER YOUR AMOUNT'))
            newUser.withDraw(amount)

        else :
            print("ENTER A VALID NUMBER")


main()        
