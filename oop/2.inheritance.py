class Animal:
    is_alive = True

    def eat(self) -> None:
        print("Eating")

    def sleep(self) -> None:
        print("zzz")


# there is no "Class2 extends Class1" or "Class2 : Class1"
# in Python you use "Class_2(Class_1)"
class Rabbit(Animal):
    def run(self):
        print("rabbit is running")


class Fish(Animal):
    def swim(self):
        print("Fish is swimming")


class Krtek(Animal):
    clothing = "kalhotky"

    pass


rabbit = Rabbit()
fish = Fish()
krtecek = Krtek()


rabbit.run()
fish.swim()
print(krtecek.clothing)
