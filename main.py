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

bus1 = Bus("BUS101", "Delhi", "Agra", 4, 500)
print(bus1.route)
print(f"{bus1.available_seats}\n{bus1.route}\n{bus1.capacity}\n{bus1.base_fare}")


