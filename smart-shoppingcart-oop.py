class Item :
    def __init__ (self,name,price) :
        self.name = name # product name 
        self.price = price # product price  
    def __str__ (self) :       
        return f"Product: {self.name} | Price: ${self.price} \n"
    def __eq__ (self,other) : ## object gula same same kina ta check korar method (# Method to check whether two objects are equal) 
        if self.name == other.name  and self.price == other.price :
            return True 
        else :
            return False 
class ShoppingCart :
    def __init__ (self,customer_name) :
        self.customer_name = customer_name
        self.items = [] 
    def add_item (self,item) :
        self.items .append(item)    
    def __len__(self) : ## size hishab korar jonno ei method (# Method to return the total number of items in the cart) 
        return len(self.items) 
    def __str__ (self) : ## user ke valo ekta message dekhanor jonno ei method(# Method to display shopping cart information) 
        total_price = 0
        for item in self.items : 
            total_price += item.price            
        return f"Customer Name: {self.customer_name} | Total Items: {len(self.items)} | Total Price: ${total_price} \n"
    def __add__ (self,other) : ## duita object summation korar jonno (# Method to merge two shopping cart objects) 
        new_customer = self.customer_name + "&" + other.customer_name 
        new_cart = ShoppingCart(new_customer) 
        new_cart.items = self.items + other.items 
        return new_cart                    
## product object create:- 
item_1=Item ("Notebooks",800)
item_2=Item ("Calculator",2400)
## every user er jonno different cart create kora (# Create separate shopping carts for each customer) :–
cart_1=ShoppingCart("Upamecano") 
cart_2=ShoppingCart("Konate")
## item list a user er product add kora (# Add products to each customer's shopping cart) :– 
cart_1.add_item(item_1)
cart_2.add_item(item_2) 
print(cart_1) ## call __str__ method 
print(len(cart_1)) ## Call  __len__ method
print(cart_2) ## call __str__  method
print(len(cart_2)) ## call __len__ method
final_cart = cart_1+cart_2 ## Merge the two shopping carts into a new cart
print(final_cart) 