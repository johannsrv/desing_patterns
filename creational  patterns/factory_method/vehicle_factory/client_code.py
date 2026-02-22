from concrete_factory import CarFactory, TruckFactory

def client_vehicle_factory(factory, vehicle_type):
    vehicle = factory.get_vehicle(vehicle_type)
    print(f"Vehicle: {vehicle.deliver()}")