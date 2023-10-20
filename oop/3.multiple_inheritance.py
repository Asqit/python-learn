# Multiple Inheritance
# is when class is derived from multiple parent classes (more than one parent class)


class Prey:
    def flee(self):
        print("rushing to safety!")


class Predator:
    def hunt(self):
        print("Just hunting for some food bruh, it's the natural order of things")


class Mouse(Prey):
    pass


class Cat(Predator):
    pass


class Fish(Prey, Predator):
    pass


# Yes, it's reversed, but I don't care this is real life
jerry = Mouse()
jerry.flee()


tom = Cat()

# Tom does not have attribute flee and causes an expetion
# > tom.flee()
tom.hunt()

# Fun Fact: sharks are bullied and hunted by dolphins :D
# +1 point for dolphins
shark = Fish()

# Has both attributes
shark.hunt()
shark.flee()
