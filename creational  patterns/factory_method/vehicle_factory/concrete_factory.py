from .creator import VehicleFactory
from .product import car, truck

class CarFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type: str):
        return car.Car(vehicle_type)

class TruckFactory(VehicleFactory):
    def get_vehicle(self, vehicle_type: str):
        return truck.Truck(vehicle_type)