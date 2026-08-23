class AccountPosition : 
### Attribiutes Initializer :-  
    def __init__ (self,account_id,balance,leverage,entry_price,current_market_price,position_size) :
        self.account_id=account_id
        self.balance=balance 
        self.leverage=leverage
        self.entry_price=entry_price
        self.current_market_price=current_market_price
        self.position_size=position_size           
 ### property decorators for leveraging (  FOR SECURITY) :- 
    @property     
    def leverage (self) :  ##getter method 
        return self.__leverage  
    @leverage.setter  
    def leverage (self,new_leverage) : # setter method         
        if 1 <= new_leverage <= 10 : 
            self.__leverage=new_leverage
        else : 
            self.__leverage=1
            alert_txt=f"[Risk Alert] Leverage out of bounds! Must be between 1x and 10x\n"   
            print(alert_txt) 
 ### Base exception for all HFT engine errors :-           
class HFTEngineError (Exception) : 
    pass  
 ### Raised immediately when account margin health drops below safety threshold :- 
class LiquidationRequiredError (HFTEngineError) : 
    pass  
### Central Risk Configuration (No Magic Numbers are required) :-      
class RiskConfiguration :
    liquidation_limit:float=0 
    default_leverage:float=1
    precision_decimal:float=2   
  ### Unrealized Profit and loss (Read-Only Computed Property) :- 
class RiskCalculatorService :       
    @staticmethod 
    def pnl (position:AccountPosition) : # 
        calculated_PnL=round((position.current_market_price-position.entry_price)*position.leverage*position.position_size,2) 
        return calculated_PnL 
 ### Calculate Total (Read Only Equity Calculator) :-     
    def calculated_total ( position:AccountPosition) : # only getter
        margin_health=round(position.balance+RiskCalculatorService.pnl(position),2) 
        return margin_health      
## Business Logic Method :-  
class TradeReportPresenter : 
    @staticmethod
    def update_market_price (new_market_price,position:AccountPosition) : 
        position.current_market_price=new_market_price
        if RiskCalculatorService.calculated_total(position) <= RiskConfiguration.liquidation_limit :
             position.position_size=0   
             raise LiquidationRequiredError (f"[LIQUIDATION] Margin depleted in 0! \nPosition auto-closed to prevent bankruptcy.\n") ## String return করার বদলে Custom Exception Raise করা    
        else :
            return f"[TRADE ACTIVE]\n Account: {position.account_id} |  Previous Market Price: ${position.entry_price} \n Price Updated to: ${new_market_price} | PnL: ${RiskCalculatorService.pnl(position)} \nMargin Health: ${RiskCalculatorService.calculated_total(position)}\n"            
### Testing Objects :-
acc_1=AccountPosition("Kroos",balance=1000,leverage=-3,entry_price=
450,current_market_price=850,position_size=2) 
print(f"Initial PnL: ${RiskCalculatorService.pnl(acc_1)}\n")
print(f"Initial Margin Health: ${RiskCalculatorService.calculated_total(acc_1)}\n")    
print(f"Initial Leverage: {acc_1.leverage}\n")  
print(TradeReportPresenter.update_market_price(200,acc_1))     