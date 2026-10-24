class Bus:
    def __init__(self, bus_number, source, destination, capacity, base_fare):
        self.bus_number = bus_number
        self.source = source
        self.destination = destination
        self.route = (source,destination)
        self.capacity = capacity
        self.base_fare = base_fare

        self.available_seats = set(range(1,capacity+1))
        self.occupied_seats = set()

class ACBus(Bus):
    def calculate_fare(self):
        return self.base_fare * 1.25

class NonACBus(Bus):
    def calculate_fare(self):
        return self.base_fare

buses = {
    "bus1": ACBus("BUS101", "Delhi", "Agra", 4, 500),
    "bus2": NonACBus("BUS102", "Delhi", "Jaipur", 5, 400),
}
for bus_number, bus in buses.items():
    print(bus_number, bus.route, bus.calculate_fare(), bus.available_seats)







