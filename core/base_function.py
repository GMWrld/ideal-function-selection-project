class BaseFunction:
    """
    Parent class representing a mathematical function.
    """

    def __init__(self, name, x_values, y_values):
        self.name = name
        self.x_values = x_values
        self.y_values = y_values

    def get_name(self):
        return self.name

    def get_x_values(self):
        return self.x_values

    def get_y_values(self):
        return self.y_values