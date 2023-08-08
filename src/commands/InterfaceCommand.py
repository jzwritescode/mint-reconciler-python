from abc import ABC, abstractmethod


class InterfaceCommand(ABC):
    @abstractmethod
    def run(self):
        """
        Run command required method
        @return: Nothing
        """
        pass
