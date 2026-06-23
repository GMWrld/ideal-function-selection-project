import numpy as np

from exceptions.custom_exceptions import (
    FunctionSelectionError
)


class FunctionSelectionService:
    """
    Selects the best ideal function
    using Least Squares.
    """

    @staticmethod
    def calculate_sse(
        training_values,
        ideal_values
    ):
        """
        Sum of Squared Errors.
        """

        differences = (
            np.array(training_values)
            - np.array(ideal_values)
        )

        return np.sum(
            differences ** 2
        )

    def find_best_fit(
        self,
        training_values,
        ideal_dataframe
    ):
        """
        Find ideal function with
        minimum SSE.
        """

        best_function = None
        lowest_sse = float("inf")

        for column in ideal_dataframe.columns:

            if column == "x":
                continue

            sse = self.calculate_sse(
                training_values,
                ideal_dataframe[column]
            )

            if sse < lowest_sse:
                lowest_sse = sse
                best_function = column

        return best_function, lowest_sse
    
    def select_all_functions(
    self,
    training_dataframe,
    ideal_dataframe
    ):
        """
        Select best ideal function
        for each training function.
        """

        results = {}

        training_columns = [
            "y1",
            "y2",
            "y3",
            "y4"
        ]

        for column in training_columns:

            best_fit, sse = self.find_best_fit(
                training_dataframe[column],
                ideal_dataframe
            )

            results[column] = {
                "ideal_function": best_fit,
                "sse": float(sse)
            }

        return results