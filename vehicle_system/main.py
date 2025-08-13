from car import Car
from bike import Bike

def main():
    car = Car("Toyota", "Corolla", 2020)
    bike = Bike("Yamaha", "MT-07", 2021)

    car.start_engine()
    car.stop_engine()

    print("---")

    bike.start_engine()
    bike.stop_engine()

if __name__ == "__main__":
    main()