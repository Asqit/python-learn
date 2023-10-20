class Animal:
    def eat(self):
        print("Animal is eating rn")


class Budgie(Animal):
    # In Python in order to override a method you must
    # define a method with the same signature, but different
    # implementation (Body)
    def eat(self):
        print("beep beep, I eat seeds UvU")

    # New! In Python 3.12 you can use "@override" decorator
    # just like it is in other languages, but the method signature
    # still has to be the same as it's ancestor's
    # > @override
    # > def eat(self):
    # >     print("eating seeds")


pepa = Budgie()
pepa.eat()
