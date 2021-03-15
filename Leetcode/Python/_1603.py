class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.count = [0, big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        self.count[carType] -= 1
        return self.count[carType] >= 0
