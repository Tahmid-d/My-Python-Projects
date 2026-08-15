class ECommerceProduct :
    def __init__ (self,name,price,stock,tax_rate) :
        self.name=name # product name
 #   direct __price / __stock না লিখে সেটারের মাধ্যমে অ্যাসাইন করা হয়েছে, যাতে অবজেক্ট তৈরির সময়ই ইনপুট ভ্যালিডেশন কাজ করে।
        self.price=price
        self.stock=stock
        self.__tax_rate=tax_rate
## Property Decorators for price (READ AND WRITE SECURITY) :-  
    @property           
    def price (self) :       
        return self.__price   
    @price.setter # getter function name .setter   
    # গেটারের ফাংশন নাম এবং সেটারের ফাংশন নাম হুবহু এক হতে হবে 
    def price (self,new_price) :     
        if new_price > 0 :           
            self.__price=new_price      
        else :
            warning_txt="Invalid Error: Price must be greater than zero!!\n"   
            print(warning_txt)          
## Property Decorators for stock (INVENTORY GUARD) :-
    @property
    def stock (self) :
        return self.__stock         
    @stock.setter # getter function name .setter 
    # গেটারের ফাংশন নাম এবং সেটারের ফাংশন নাম হুবহু এক হতে হবে 
    def stock (self,new_stock) :
        if new_stock >= 0 : 
            self.__stock=new_stock 
        else :
            alert_txt=f"Error: Stock cannot be negative!\n" 
            print(alert_txt)
 ## Read Only Dynamic Calculator :-
    @property 
    def final_price (self) :        
         calculated_price=self.__price+(self.__price*(self.__tax_rate/100)) 
         return round(calculated_price,3) 
 ## Business Logic :-
    def purchase (self,quantity) :
        if quantity <= self.stock :
            total_price=round(quantity*self.final_price,3) 
            self.stock -= quantity 
            return f"Product: {self.name} | Total Price: {total_price} | Remaining Stock: {self.stock}\n" 
        else :
            error_txt=f"Not enough stock available!\n"
            return error_txt  
## Testing Objects :-
p1=ECommerceProduct("BOOK",400,8,3) # product 1 
p2=ECommerceProduct("Keyboard",750,10,1.5) # product 2 
## Information Show :- 
print(p1.price) 
print(p2.price)  
## Setter and Data Update :- 
p1.price=360 
p2.price=580
p2.stock=8 
p1.stock=6
p1.price=-2000
## Call the purchase method :- 
print(p1.purchase(4))  
print(p2.purchase(3))                                                                                                                               