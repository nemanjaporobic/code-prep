# Adapter is a structural design pattern, which allows incompatible objects to collaborate.
#
# The Adapter acts as a wrapper between two objects. It catches calls for one object and transforms them to format
# and interface recognizable by the second object.
#
# Complexity: x
# Popularity: xxx
#
# Usage examples: The Adapter pattern is pretty common in Python code. It’s very often used in systems based on some
# legacy code. In such cases, Adapters make legacy code work with modern classes.
#
# Identification: Adapter is recognizable by a constructor which takes an instance of a different abstract/interface
# type. When the adapter receives a call to any of its methods, it translates parameters to the appropriate format
# and then directs the call to one or several methods of the wrapped object.
#
# Conceptual Example (via inheritance)
# Conceptual Example (via object composition)
# Conceptual Example (via inheritance)
# This example illustrates the structure of the Adapter design pattern. It focuses on answering these questions:
#
# What classes does it consist of?
# What roles do these classes play?
# In what way the elements of the pattern are related?
#  main.py: Conceptual example

class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)