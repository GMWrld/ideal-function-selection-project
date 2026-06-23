from core.base_function import BaseFunction


class IdealFunction(BaseFunction):
    """
    Represents an ideal function.
    """

    def __init__(
        self,
        name,
        x_values,
        y_values
    ):
        super().__init__(
            name,
            x_values,
            y_values
        )