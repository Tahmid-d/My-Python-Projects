class Item : 
    def __init__ (self,name,item_id,title) : 
        self.name = name 
        self.item_id = item_id 
        self.title = title         
        self.__is_borrowed = False ## library ta boita ache

  ## ​Getter method: প্রাইভেট ভ্যারিয়েবল __is_borrowed-এর মান কী (True নাকি False) তা সেফলি দেখার জন্য এই মেথড ব্যবহার করা হয়েছে।   
    def is_borrowed_status (self) :
        print(f"[STATUS] Reader: {self.name} (ID: {self.item_id}) | Selected Item: '{self.title}'\n") 
        return self.__is_borrowed
    def cashout_check (self) : ## Setter method: বই বা ডিভিডি ধার দেওয়ার সময় __is_borrowed-এর মান False থেকে True-তে পরিবর্তন করার লজিক এখানে লেখা হয়েছে
       if self.__is_borrowed == False : 
           self.__is_borrowed = True 
           print(f"[SUCCESS] Hi {self.name}, '{self.title}' is available! Borrowed successfully.\n")          
       else : 
           self.__is_borrowed = True 
           print(f"[UNAVAILABLE] Sorry {self.name}, '{self.title}' is currently borrowed by someone else.\n")    
    def return_item (self) : 
        if self.__is_borrowed == True : 
            self.__is_borrowed = False 
            print(f"[RETURN SUCCESS] '{self.title}' has been successfully returned to the library.\n")         
        else : 
            print(f"[RETURN ERROR] Action failed! '{self.title}' was not borrowed from this library.\n") 
## child class 1 :- 
class Book (Item) : 
    def __init__ (self,name,item_id,title,author,page_count) : 
        super().__init__ (name,item_id,title)  
        self.author = author
        self.page_count = page_count 
    def calculate_late_fee (self,late_days) :
        book_late_fee = 20 
        total_fees = late_days*book_late_fee
        print(f"[LATE FEE - BOOK] Reader: {self.name} (ID: {self.item_id})\n"
              f"Category: '{self.title}' | Author: {self.author} ({self.page_count} pages)\n"
              f"Overdue Days: {late_days} | Daily Charge: ${book_late_fee} | Total Due: ${total_fees}\n")  
class DVD (Item) : 
    def __init__  (self,name,item_id,title,director,duration) : 
        super().__init__ (name,item_id,title)  
        self.director = director   
        self.duration = duration 
    def calculate_late_fee (self,late_days) : 
       dvd_late_fee = 40 
       total_fees = late_days*dvd_late_fee      
       print(f"[LATE FEE - DVD] Customer: {self.name} (ID: {self.item_id})\n"
              f"Category: '{self.title}' | Director: {self.director} ({self.duration} mins)\n"
              f"Overdue Days: {late_days} | Daily Charge: ${dvd_late_fee} | Total Due: ${total_fees}\n") 
# testing object 
book_1= Book ("Raheem","0129rah","Book","Naim Uddin",9) 
dvd_1= DVD ("Iqbal Hossain","999iqbal","DVD","Mr.Asif Raihan",40)
book_2= Book ("Yeashin","yashin002","Book","Mr. Tahmid Amin",10) 
dvd_2 = DVD ("Iker Casillas","casillas11","DVD","Md. Asif Mahmud",50)

book_1.cashout_check()  
dvd_1.calculate_late_fee(4)
book_2.calculate_late_fee(9)
dvd_2.calculate_late_fee(8)   