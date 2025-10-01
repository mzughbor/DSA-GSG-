from vehicle import Vehicle

class Car(Vehicle):
    def start_engine(self) -> None:
        print(f"The {self.make} - {self.year} - {self.model} car's engine has started.")

    def stop_engine(self) -> None:
        print(f"The {self.make} - {self.year} - {self.model} car's engine has stopped.")