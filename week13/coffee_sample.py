class Coffee:
    def __init__(self, coffee_type, size, milk, flavor, pumps):
        # Private attributes protect the order details
        self.__coffee_type = coffee_type
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__pumps = pumps

    # --- Getters ---
    def get_coffee_type(self):
        return self.__coffee_type

    def get_pumps(self):
        return self.__pumps

    # --- Setters ---
    def set_pumps(self, pumps):
        # Setters allow us to validate data before changing it
        if pumps >= 0:
            self.__pumps = pumps

    # --- Summary Output ---
    def get_summary(self):
        return (f"Order Summary: {self.__size} {self.__coffee_type} "
                f"with {self.__milk} milk, {self.__flavor} flavor, "
                f"and {self.__pumps} pumps.")

# Using the objects
coffee1 = Coffee("Latte", "Large", "Whole", "Vanilla", 3)
print(coffee1.get_summary())