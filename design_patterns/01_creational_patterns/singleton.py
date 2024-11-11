# Singleton has almost the same pros and cons as global variables. Although they’re super-handy,
# they break the modularity of your code.
#
# You can’t just use a class that depends on a Singleton in some other context, without carrying over the Singleton
# to the other context. Most of the time, this limitation comes up during the creation of unit tests.
#
# Complexity: x
# Popularity: xx
#
# Usage examples: A lot of developers consider the Singleton pattern an antipattern. That’s why its usage
# is on the decline in Python code.
#
# Identification: Singleton can be recognized by a static creation method, which returns the same cached object.

# Naïve Singleton
# It’s pretty easy to implement a sloppy Singleton. You just need to hide the constructor and implement
# a static creation method.
#
# The same class behaves incorrectly in a multithreaded environment. Multiple threads can call the creation
# method simultaneously and get several instances of Singleton class.


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")