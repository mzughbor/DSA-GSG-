class Product:
    """
    A base class for all products in the vending machine.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        """
        Displays the basic product information.
        """
        return f"Product: {self.name}, Price: ${self.price:.2f}"


class Drink(Product):
    """
    A subclass for drink products.
    """
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def display_info(self):
        """
        Overrides the base class method to include volume information.
        """
        return f"{super().display_info()}\nVolume: {self.volume}ml"


class Snack(Product):
    """
    A subclass for snack products.
    """
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

    def display_info(self):
        """
        Overrides the base class method to include calorie information.
        """
        return f"{super().display_info()}\nCalories: {self.calories}"


class Candy(Product):
    """
    A subclass for candy products.
    """
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor

    def display_info(self):
        """
        Overrides the base class method to include flavor information.
        """
        return f"{super().display_info()}\nFlavor: {self.flavor}"


def load_products(filename):
    """
    Loads products from a text file and creates the corresponding objects.
    """
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                product_type = parts[0].strip()
                name = parts[1].strip()
                price = float(parts[2].strip())
                attribute = parts[3].strip()

                if product_type == "Drink":
                    volume = int(attribute)
                    products.append(Drink(name, price, volume))
                elif product_type == "Snack":
                    calories = int(attribute)
                    products.append(Snack(name, price, calories))
                elif product_type == "Candy":
                    flavor = attribute
                    products.append(Candy(name, price, flavor))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    return products


def main():
    """
    Main function to run the vending machine simulation.
    """
    # Create a dummy products.txt file for demonstration
    with open('products.txt', 'w') as f:
        f.write("Drink, Cola, 1.50,500\n")
        f.write("Snack, Chips, 2.00,250\n")
        f.write("Candy, Gummy Bears, 1.20, Strawberry\n")
        f.write("Drink, Water, 1.00,600\n")
        f.write("Snack, Cookies, 1.75,300\n")

    products = load_products("products.txt")
    if products is None:
        return

    print("Welcome to the Python Vending Machine! 👋")
    while True:
        print("\nPlease select what you want:")
        for i, product in enumerate(products):
            print(f"{i + 1}. {type(product).__name__}  {product.name}")

        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(products):
                selected_product = products[choice]
                print("\nProduct Information:")
                print(selected_product.display_info())
                break
            else:
                print("Invalid selection. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from the list.")


if __name__ == "__main__":
    main()