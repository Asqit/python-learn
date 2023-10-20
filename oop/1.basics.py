class Car:
    # static variable
    wheels = 4

    # this is how constructors look in Python
    def __init__(self, make: str, model: str, year: int, color: str) -> None:
        # instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # the "self" is reference to the object constructed from this class
    # basically "this" keyword in other languages, see Rust's structures...
    def drive(self) -> None:
        print(f"The {self.model} is currently driving")

    def stop(self) -> None:
        print(f"The {self.model} is stopped")

    def static_method():
        print("I am static method on Car class")


# There is no "new" keyword, just execute it like a function
car_1 = Car("BMW", "316i", 1996, "Violetrott")
car_1.drive()

# Acessing static properties
print(car_1.wheels)
Car.static_method()

# If you try executing an instance method as static
# you'll get TypeError: missing 1 required positional argument: "self"
# > Car.drive()
