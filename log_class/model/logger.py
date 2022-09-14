from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def get_info(self, message, object): pass

    @abstractmethod
    def get_warning(self, message, object): pass

    @abstractmethod
    def get_error(self, message, object): pass

    @abstractmethod
    def get_debug(self, message, object): pass
