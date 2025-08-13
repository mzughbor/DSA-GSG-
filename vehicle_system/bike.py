from vehicle import Vehicle

class Bike(Vehicle):
    def start_engine(self) -> None:
        print(f"The {self.make} - {self.year} - {self.model} bike's engine has started.")

    def stop_engine(self) -> None:
        print(f"The {self.make} - {self.year} - {self.model} bike's engine has stopped.")