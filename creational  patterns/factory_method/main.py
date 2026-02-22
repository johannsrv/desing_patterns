from vehicle_factory.client_code import client_vehicle_factory

if __name__ == "__main__":
    print("Client: Testing client code with the CarFactory:")
    client_vehicle_factory(CarFactory(), "Sedan")

    print("\nClient: Testing the same client code with the TruckFactory:")
    client_vehicle_factory(TruckFactory(), "Pickup")