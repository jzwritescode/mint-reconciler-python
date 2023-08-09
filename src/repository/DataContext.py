class DataContext:
    """
    Stores data being loaded from each data file type
    """
    def __init__(self, keys: list = None):
        if keys is None:
            self.keys = []
        self.keys = keys
        self.data_context = {}
        for key in self.keys:
            self.data_context[key] = []
