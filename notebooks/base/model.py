from abc import abstractclassmethod

class BaseObject:
    def __init__(self, name: str):
        self.name = name
        self.is_fit = False

    def fit(self) -> None:
        self.is_fit = True
        print('Fitted Object Properly')


class BaseProcessor:
    def __init__(self, name: str, bounded_object: BaseObject, expected_object_type: type = BaseObject):
        if type(bounded_object) != expected_object_type:
            raise Exception(f"Object passed is not {expected_object_type}!")
        if not bounded_object.is_fit:
            raise Exception("Object passed is not fit!")
        self.name = name
        self.bounded_object = bounded_object
        


class BaseProcessorFactory:
    def __init__(self, name: str, bounded_object: BaseObject, expected_object_type: type = BaseObject):
        self.name = name
        self.expected_object_type = expected_object_type
        self.bounded_object = bounded_object