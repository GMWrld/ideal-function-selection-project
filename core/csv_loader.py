import pandas as pd

from exceptions.custom_exceptions import CSVLoadError


class CSVLoader:
    """
    Handles loading and validation
    of CSV datasets.
    """

    @staticmethod
    def load_csv(file_path):
        """
        Load a CSV file and return
        a pandas DataFrame.
        """

        try:
            df = pd.read_csv(file_path)

            if df.empty:
                raise CSVLoadError(
                    f"{file_path} is empty."
                )

            return df

        except FileNotFoundError:
            raise CSVLoadError(
                f"{file_path} not found."
            )

        except Exception as e:
            raise CSVLoadError(
                f"Error loading {file_path}: {e}"
            )