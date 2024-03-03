class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Максимальна швидкість: {self.max_speed} км/год")

vehicle1 = TransportVehicle("Автомобіль", 200)

vehicle1.display_info()


class Plane(TransportVehicle):
    def __init__(self, name, max_speed, flight_range):
        super().__init__(name, max_speed)
        self.flight_range = flight_range

    def display_info(self):
        super().display_info()
        print(f"Дальність польоту: {self.flight_range} км")

plane1 = Plane("Боїнг 747", 900, 14000)

plane1.display_info()


