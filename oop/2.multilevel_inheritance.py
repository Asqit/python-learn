# Multi-level Inheritance
# Is when a derived class inherits from another derived class (derived ~ children)


class Organism:
    """Top parent"""

    is_alive = True


class Animal(Organism):
    """First child"""

    def eat(self) -> None:
        print("Animal is eating")


class Budgie(Animal):
    """second child"""

    def sing(self):
        print("This budgie is singing")


pepa = Budgie()

print(pepa.is_alive)
pepa.eat()
pepa.sing()
