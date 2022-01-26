from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError
        
    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass        
    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFashionPrinter(Machine):
    def print(self, document): # OK
        pass        
    def fax(self, document): # KO
        pass

    def scan(self, document): # KO
        pass

# Solution
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass
    def scan(self, document):
        pass