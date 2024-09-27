#base class
class DataGenerator:
    def generate(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")
