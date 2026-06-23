from core.base_function import BaseFunction


class TrainingFunction(BaseFunction):
    """
    Represents a training function.
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