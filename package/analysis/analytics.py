from abc import abstractmethod
from base import model

from base.model import BaseObject
from base.model import BaseProcessor
from base.model import BaseProcessorFactory

class AnalyticsObject(BaseObject):
    def __init__(self, name):
        super().__init__(name + " Object")


class AnalyticsProcessorFactory(BaseProcessorFactory):
    def __init__(self, name: str, bounded_object: AnalyticsObject, expected_object_type: type = BaseObject):
        super().__init__(name + " Analyzer", bounded_object, AnalyticsObject)

    @abstractmethod
    def create_analyzer(self, bounded_object: AnalyticsObject):
        pass

    @abstractmethod
    def create_grapher(self, bounded_object: AnalyticsObject):
        pass

class AnalyticsAnalyzer(BaseProcessor):
    def __init__(self, name, bounded_object: AnalyticsObject, expected_object_type: type = BaseObject):
        super().__init__(name + " Analyzer", bounded_object, expected_object_type)

class AnalyticsGrapher(BaseProcessor):
    def __init__(self, name, bounded_object: AnalyticsObject, expected_object_type: type = BaseObject):
        super().__init__(name + " Grapher", bounded_object, expected_object_type)