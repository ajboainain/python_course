
class Vehicle:
    vehicle_details = {}

    def __init__(self, eating_capacity, fuel, wheels):
        self.vehicle_details = {
            "eating_capacity": eating_capacity,
            "fuel": fuel,
            "wheels": wheels,
        }

    def details(self):
        return self.vehicle_details


car = Vehicle(10, "petrol", 4)

print(car.details())
