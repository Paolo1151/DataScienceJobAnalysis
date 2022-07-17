from abc import abstractmethod
from base import model

class AnalyticsObject(model.BaseObject):
    def __init__(self, name):
        super().__init__(name + " Object")


class AnalayticsProcessorFactory(model.BaseProcessorFactory):
    def __init__(self, name: str, bounded_object: model.BaseObject, expected_object_type: type = model.BaseObject):
        super().__init__(name + " Analyzer", bounded_object, AnalyticsObject)

    @abstractmethod
    def create_analyzer(self, bounded_object: AnalyticsObject):
        pass
    
    @abstractmethod
    def create_grapher(self, bounded_object: AnalyticsObject):
        pass 


class AnalyticsAnalyzer(model.BaseProcessor):
    def __init__(self, name, bounded_object: AnalyticsObject):
        super().__init__(name + " Analyzer", bounded_object, AnalyticsObject)

    @abstractmethod
    def analyze(self):
        pass

class AnalyticsGrapher(model.BaseProcessor):
    def __init__(self, name, bounded_object: AnalyticsObject):
        super().__init__(name + " Grapher", bounded_object, AnalyticsObject)

    @abstractmethod
    def graph(self):
        pass

    


