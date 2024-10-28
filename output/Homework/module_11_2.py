def introspection_info(obj):
    info = {'type': type(obj).__name__}

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['methods'] = methods

    info['module'] = obj.__module__ if hasattr(obj, '__module__') else 'нет модуля'

    return info


class SampleClass:

    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"


obj_1 = SampleClass('rome')
class_info = introspection_info(obj_1)
print(class_info)
print(obj_1.display())
obj_2 = 42
class_info_1 = introspection_info(obj_2)
print(class_info_1)
