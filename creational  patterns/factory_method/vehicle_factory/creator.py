from abc impot ABC, abstractmethod
from .product import car, truck

class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self, vehicle_type: str):
        pass


