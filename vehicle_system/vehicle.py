from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        pass