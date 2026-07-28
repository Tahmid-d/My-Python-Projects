from abc import ABC, abstractmethod
## Abstract class:- 
class Ride (ABC) :
    def __init__ (self,passenger_name,driver_name,distance_km) :
        self.passenger_name = passenger_name
        self.driver_name = driver_name
        self.distance_km = distance_km 
    @abstractmethod 
    def calculate_fare (self) :
        pass
    @abstractmethod  
    def start_trip (self) :
        pass 
## child class 1:-
class BikeRide (Ride) :
    def __init__ (self,passenger_name,driver_name,distance_km) : 
        super(). __init__ (passenger_name,driver_name,distance_km) 
    def calculate_fare (self) :
        base_fare = 50
        per_km_fare = 20 
        total_fare = base_fare + (self.distance_km*per_km_fare) 
        print(f"[FARE SUMMARY - BIKE] Distance: {self.distance_km} km | Base: ${base_fare} | Per KM: ${per_km_fare}\n Total Payable Fare: ${total_fare}\n")          
    def start_trip (self) :
        print(f"[RIDE STARTED]️ Passenger: {self.passenger_name} | Driver: {self.driver_name} \n(Category: Bike)\n Have a safe journey!")   
## child class 2:- 
class CarRide (Ride) :
    def __init__ (self,passenger_name,driver_name,distance_km,is_ac) :        
        super().__init__ (passenger_name,driver_name,distance_km) 
        self.is_ac = is_ac 
    def calculate_fare (self) :
        base_fare = 80   
        per_km_fare = 30 
        if self.is_ac == True :
            ac_fare = 40
            total_fare = base_fare + (per_km_fare*self.distance_km) + ac_fare 
            print(f"[FARE SUMMARY - CAR] Distance: {self.distance_km} km | Base: ${base_fare} | Per KM: ${per_km_fare} | AC Charge: ${ac_fare}\n Total Payable Fare: ${total_fare}\n")  
        else : 
            non_ac_fare = 0 
            total_fare = base_fare + (per_km_fare*self.distance_km) + non_ac_fare 
            print(f"[FARE SUMMARY - CAR] Distance: {self.distance_km} km | Base: ${base_fare} | Per KM: ${per_km_fare} | AC Charge: ${non_ac_fare}\n Total Payable Fare: ${total_fare}\n")      
    def start_trip (self) :
        print(f"[RIDE STARTED] Passenger: {self.passenger_name} | Driver: {self.driver_name} \n(Category: Car - AC)\n Have a comfortable journey!")  
## child class 3:- 
class CNGRide (Ride) :
    def __init__ (self,passenger_name,driver_name,distance_km)  :  
        super().__init__ (passenger_name,driver_name,distance_km)  
    def calculate_fare (self) :
        base_fare = 20 
        per_km_fare = 10 
        total_fare = base_fare + (per_km_fare*self.distance_km)  
        print(f"[FARE SUMMARY - CNG] Distance: {self.distance_km} km | Base: ${base_fare} | Per KM: ${per_km_fare}\n Total Payable Fare:${total_fare}\n")       
    def start_trip (self) :
        print(f"[RIDE STARTED] Passenger: {self.passenger_name} | Driver: {self.driver_name} \n(Category: CNG)\n Enjoy your ride!") 
## Testing Objects:- 
rider_1 = BikeRide ("Hugo Lloris","Mr.Jihad",11)
rider_2 = CarRide ("William Saliba","Mr.Akbar Ali",18,True)  
rider_3 = CNGRide ("Hujisen","Mr.Nazim Shah",5)   
rider_1.start_trip() 
rider_1.calculate_fare()
rider_2.start_trip()
rider_2.calculate_fare()
rider_3.start_trip()  
rider_3.calculate_fare()                                           
                              