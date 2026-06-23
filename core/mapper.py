import numpy as np


class MappingService:
    """
    Handles assignment of test points
    to ideal functions.
    """

    @staticmethod
    def calculate_max_deviation(
        training_values,
        ideal_values
    ):
        """
        Maximum absolute deviation.
        """

        differences = np.abs(
            np.array(training_values)
            - np.array(ideal_values)
        )

        return float(
            np.max(differences)
        )
    @staticmethod
    def calculate_threshold(
        max_deviation
    ):
        """
        Assignment threshold.
        """

        return float(
            max_deviation * np.sqrt(2)
        )
    
    @staticmethod
    def calculate_test_deviation(
        test_y,
        ideal_y
    ):
        """
        Deviation between a test point
        and an ideal function value.
        """

        return float(
            abs(test_y - ideal_y)
        )
    
    def map_point(
    self,
    x_value,
    test_y,
    ideal_df,
    thresholds
    ):
        """
        Map a single test point to the best
        matching ideal function.
        """

        row = ideal_df[
            np.isclose(
                ideal_df["x"],
                x_value
            )
        ]

        if row.empty:
            return None

        best_function = None
        best_deviation = float("inf")

        for ideal_function, threshold in thresholds.items():

            ideal_y = row.iloc[0][ideal_function]

            deviation = self.calculate_test_deviation(
                test_y,
                ideal_y
            )

            if deviation <= threshold:

                if deviation < best_deviation:

                    best_deviation = deviation
                    best_function = ideal_function

        if best_function is None:
            return None

        return {
            "ideal_function": best_function,
            "delta_y": best_deviation
        }
    
    def map_all_points(
    self,
    test_df,
    ideal_df,
    thresholds
    ):
        """
        Process entire test dataset.
        """

        results = []

        for _, row in test_df.iterrows():

            result = self.map_point(
                row["x"],
                row["y"],
                ideal_df,
                thresholds
            )

            if result:

                results.append({
                    "x": float(row["x"]),
                    "y": float(row["y"]),
                    "ideal_function":
                        result["ideal_function"],
                    "delta_y": float(result["delta_y"])
                })

        return results