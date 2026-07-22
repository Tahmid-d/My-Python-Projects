# # মূল ব্যাংকিং ইঞ্জিন (প্যারেন্ট ক্লাস) 
class BaseAccount : 
    def __init__ (self,account_holder,account_balance) : 
    ## অ্যাকাউন্টের হোল্ডারের নাম (public) এবং একাউন্ট ব্যালেন্স (private) :‐ 
        self.account_holder=account_holder
        self.__account_balance = account_balance
    def get_balance (self) : 
    ## বর্তমান ব্যালেন্স প্রিন্ট করে দেখানোর এবং তা রিটার্ন করার মেথড :‐ 
        print(f"[Account Status] Holder: {self.account_holder} | Current Balance: ${self.__account_balance}\n") 
        return self.__account_balance 
    def set_balance (self,new_acc_balance) : 
    ## ব্যালেন্স আপডেট করার সময় তা নেগেটিভ কি না ভ্যালিডেশন চেক করা হচ্ছে; new_acc_balance = তোলা টাকার পরিমাণ 
        if new_acc_balance >= 0 : 
            self.__account_balance =  new_acc_balance    
            print(f"[Success] Balance updated successfully for {self.account_holder}. New Balance: ${self.__account_balance}\n")  
        else : 
            print(f"[Error] Transaction Failed! Deposit amount must be greater than $0.\n") 
        print(f"Account holder name is: {self.account_holder}. {self.account_holder} account balance is: {self.__account_balance}\n")      
    def withdraw (self,new_acc_balance) : 
    ## সাধারণ অ্যাকাউন্ট থেকে টাকা তোলার সময় পর্যাপ্ত ব্যালেন্স এবং অ্যামাউন্ট জিরো থেকে বড় কি না শর্ত যাচাই:- 
        if new_acc_balance <= self.__account_balance and new_acc_balance > 0 :    
            final_balance =  self.__account_balance - new_acc_balance     
            final_balance = self.__account_balance    
            print(f"[Success] Withdrawn: ${new_acc_balance} | Remaining Balance: ${final_balance}\n")      
        else : 
            print(f"[Error] Withdrawal Failed! Insufficient funds or invalid amount.\n")
## সেভিংস অ্যাকাউন্ট ক্লাস (ইনহেরিটেন্সের ব্যবহার)             
class SavingsAccount (BaseAccount) : 
    def __init__ (self, account_holder, account_balance) : 
 ## super() এর মাধ্যমে প্যারেন্ট ক্লাসের কনস্ট্রাক্টর কল করা হয়েছে:- 
        super().__init__ (account_holder,account_balance) 
    def withdraw (self,new_acc_balance) : 
## সেভিংস অ্যাকাউন্ট থেকে টাকা তোলার লজিক ওভাররাইড করা হয়েছে (এখানে নির্দিষ্ট সার্ভিস চার্জ যুক্ত হয়):-     
        current_balance = self.get_balance() 
        charge = 100 
        total_balance = new_acc_balance + charge 
## মূল ব্যালেন্সের সাথে চার্জ যোগ করার পর পর্যাপ্ত ফান্ড আছে কি না তা চেক করা:-         
        if total_balance <= current_balance and total_balance > 0 : 
            update_balance = current_balance - charge 
            self.set_balance (update_balance) 
            print(f"[Savings Account] Cashout: ${new_acc_balance} | Charge: ${charge} | Remaining Balance: ${update_balance}\n")             
        else : 
            print(f"[Error] Transaction Declined! You need ${total_balance} (including $100 charge), but available balance is ${current_balance}.\n") 
## ভিআইপি অ্যাকাউন্ট ক্লাস (পলিমরফিজম ও কাস্টম রুলস):–             
class VIPAccount (BaseAccount) : 
    def __init__ (self, account_holder, account_balance) : 
        super().__init__(account_holder,account_balance) 
    def withdraw (self,new_acc_balance) :
## ভিআইপি অ্যাকাউন্টের জন্য বিশেষ লিমিট এবং প্রিভিলেজ রুলস সেট করা হয়েছে:–         
        current_balance = self.get_balance() 
        vip_limit = 15000
## উইথড্র করার অ্যামাউন্ট ভিআইপি লিমিটের মধ্যে এবং জিরো থেকে বড় কি না চেক করা:-         
        if new_acc_balance <= vip_limit and new_acc_balance > 0 :     
            update_balance = current_balance - new_acc_balance     
            self.set_balance (update_balance)   
            print(f"[VIP Privilege] No extra charges applied. Cashout: ${new_acc_balance} | Remaining Balance: ${update_balance}.\n")             
        else : 
            print(f"[VIP Limit Exceeded] Single withdrawal limit is: ${vip_limit}. Requested: ${new_acc_balance}\n") 
## অবজেক্ট তৈরি এবং টেস্ট কেস রান করা (Testing Objects):- 
account_1 = SavingsAccount ("Nikhil",5000)  
account_2 = SavingsAccount ("Nahian",7500)   
account_3 = VIPAccount ("Desirè",14000)
account_4 = VIPAccount ("Tahmid",15600) ##  বিভিন্ন অ্যাকাউন্টে পলিমরফিক উইথড্র মেথড কল করা হচ্ছে:- 
account_1.withdraw(5000) 
account_2.withdraw(-4000)
account_3.withdraw(13100) 
account_4.withdraw(14999)      