class HFTRiskEngine :
  ## Attribiutes Initializer :- 
    def __init__ (self,account_id,balance,leverage,entry_price,current_market_amount,position_size) :
        self.account_id=account_id
        self.balance=balance 
        self.leverage=leverage
        self.entry_price=entry_price
        self.current_market_amount=current_market_amount
        self.position_size=position_size 
  ## property decorators for leveraging ( SECURITY) :- 
    @property 
    def leverage (self) : # getter method 
        return self.__leverage
    @leverage.setter 
    def leverage (self,new_leverage) : # setter method 
        if 1 <= new_leverage <= 10 : 
            self.__leverage=new_leverage
        else : 
            self.__leverage=1           
            alert_txt=f"[Risk Alert] Leverage out of bounds! Must be between 1x and 10x.\n" 
            print(alert_txt) 
 ## Property Decorators for Unrealized Profit and loss (Property Read-Only Computed Property) :-  
    @property 
    def pnl (self) : # only getter 
        calculated_PnL=round((self.current_market_amount-self.entry_price)*self.__leverage*self.position_size,2) 
        return calculated_PnL
 ## Calculate Total (Read Only Equity Calculator) :- 
    @property
    def calculated_total (self) : # only getter
        margin_health=round(self.balance+self.pnl,2) 
        return margin_health 
## Business Logic Method :- 
    def update_market_price (self,new_market_price) :
        self.current_market_amount=new_market_price 
        if self.calculated_total <= 0 :
            warning_txt=f"[LIQUIDATION] Margin depleted in 0! \nPosition auto-closed to prevent bankruptcy.\n"   
            self.position_size=0               
            return warning_txt
        else :
            return f"[TRADE ACTIVE]\n Account: {self.account_id} |  Previous Market Price: ${self.entry_price} \n Price Updated to: ${self.current_market_amount} | PnL: ${self.pnl} \nMargin Health: ${self.calculated_total}\n"            
## Testing Objects :-
acc_1=HFTRiskEngine("Kroos",balance=1000,leverage=1,entry_price=
450,current_market_amount=850,position_size=2) 
print(f"Initial PNL: ${acc_1.pnl}\n")  
print(f"Initial Margin Health: ${acc_1.calculated_total}\n")    
print(f"Initial Leverage: {acc_1.leverage}\n")  
print(acc_1.update_market_price(300))  