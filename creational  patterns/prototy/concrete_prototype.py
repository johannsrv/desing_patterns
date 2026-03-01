import copy
from prototype import Prototype

class SystemCopy(Prototype):
    def __init__(self, configuration):
        self.configuration = configuration
    
    def clone(self):
        return copy.deepcopy(self)






