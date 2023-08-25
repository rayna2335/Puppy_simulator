import abc

class Puppy_State(abc.ABC):
    """ Interface """
    @abc.abstractmethod
    def play(self, puppy):
        pass

    @abc.abstractmethod
    def feed(self, puppy):
        pass