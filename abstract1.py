from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,name,colour,price):
        self.name=name
        self.colour=colour
        self.price=price
        self.speed=0
        
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def speed_up(self):
        pass
    @abstractmethod
    def speed_down(self):
        pass

class Bmw(Car):
    def speed_up(self):
        self.speed+=5
    def stop(self):
        self.speed=0
    def speed_down(self):
        self.speed-=5
    
bmw=Bmw("xyz","black",20000)
