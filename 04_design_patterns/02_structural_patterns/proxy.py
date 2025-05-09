# Proxy is a structural design pattern that provides an object that acts as a substitute for a real service object
# used by a client. A proxy receives client requests, does some work (access control, caching, etc.) and then passes
# the request to a service object.
#
# The proxy object has the same interface as a service, which makes it interchangeable with a real object when passed
# to a client.
#
# Complexity: xx
# Popularity: x
#
# Usage examples: While the Proxy pattern isn’t a frequent guest in most Python applications, it’s still very handy
# in some special cases. It’s irreplaceable when you want to add some additional behaviors to an object of some
# existing class without changing the client code.
#
# Identification: Proxies delegate all of the real work to some other object. Each proxy method should, in the end,
# refer to a service object unless the proxy is a subclass of a service.
#
# Conceptual Example
# This example illustrates the structure of the Proxy design pattern. It focuses on answering these questions:
#
# What classes does it consist of?
# What roles do these classes play?
# In what way the elements of the pattern are related?


from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)