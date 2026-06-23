from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import TestMapping
from database.models import TestData

from database.models import (
    Base,
    TrainingData,
    IdealFunctionData,
    TestMapping
)


class DatabaseManager:
    """
    Handles SQLite database creation and session management.
    """

    def __init__(self, db_name="ideal_functions.db"):
        self.db_name = db_name

        self.engine = create_engine(
            f"sqlite:///{self.db_name}"
        )

        self.Session = sessionmaker(
            bind=self.engine
        )

    def create_database(self):
        """
        Create all tables defined in models.py
        """
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """
        Return a database session.
        """
        return self.Session()
    
    def save_training_data(self, dataframe):
        """
        Save training dataset into SQLite.
        """

        session = self.get_session()

        try:
            for _, row in dataframe.iterrows():
                record = TrainingData(
                    x=row["x"],
                    y1=row["y1"],
                    y2=row["y2"],
                    y3=row["y3"],
                    y4=row["y4"]
                )

                session.add(record)

            session.commit()

        finally:
            session.close()
            

    def clear_training_data(self):

        session = self.get_session()

        try:

            session.query(TrainingData).delete()
            session.commit()

        finally:

            session.close()


    def save_mapping_results(
    self,
    mapping_results
    ):
        """
        Save mapped test points.
        """

        session = self.get_session()

        try:

            for row in mapping_results:

                record = TestMapping(
                    x=row["x"],
                    y=row["y"],
                    delta_y=row["delta_y"],
                    ideal_function=row["ideal_function"]
                )

                session.add(record)

            session.commit()

        finally:

            session.close()

    def clear_mapping_results(self):
        """
        Remove existing mapping results.
        """

        session = self.get_session()

        try:

            session.query(
                TestMapping
            ).delete()

            session.commit()

        finally:

            session.close()

    def save_ideal_data(self, dataframe):
        """
        Save ideal functions dataset into SQLite.
        """

        session = self.get_session()

        try:

            for _, row in dataframe.iterrows():

                record = IdealFunctionData(
                    x=row["x"],

                    y1=row["y1"],
                    y2=row["y2"],
                    y3=row["y3"],
                    y4=row["y4"],
                    y5=row["y5"],
                    y6=row["y6"],
                    y7=row["y7"],
                    y8=row["y8"],
                    y9=row["y9"],
                    y10=row["y10"],

                    y11=row["y11"],
                    y12=row["y12"],
                    y13=row["y13"],
                    y14=row["y14"],
                    y15=row["y15"],
                    y16=row["y16"],
                    y17=row["y17"],
                    y18=row["y18"],
                    y19=row["y19"],
                    y20=row["y20"],

                    y21=row["y21"],
                    y22=row["y22"],
                    y23=row["y23"],
                    y24=row["y24"],
                    y25=row["y25"],
                    y26=row["y26"],
                    y27=row["y27"],
                    y28=row["y28"],
                    y29=row["y29"],
                    y30=row["y30"],

                    y31=row["y31"],
                    y32=row["y32"],
                    y33=row["y33"],
                    y34=row["y34"],
                    y35=row["y35"],
                    y36=row["y36"],
                    y37=row["y37"],
                    y38=row["y38"],
                    y39=row["y39"],
                    y40=row["y40"],

                    y41=row["y41"],
                    y42=row["y42"],
                    y43=row["y43"],
                    y44=row["y44"],
                    y45=row["y45"],
                    y46=row["y46"],
                    y47=row["y47"],
                    y48=row["y48"],
                    y49=row["y49"],
                    y50=row["y50"]
                )

                session.add(record)

            session.commit()

        finally:

            session.close()

    def clear_ideal_functions(self):
        """
        Remove existing ideal functions.
        """

        session = self.get_session()

        try:

            session.query(
                IdealFunctionData
            ).delete()

            session.commit()

        finally:

            session.close()

    def save_test_data(self, dataframe):
        """
        Save test dataset into SQLite.
        """

        session = self.get_session()

        try:

            for _, row in dataframe.iterrows():

                record = TestData(
                    x=row["x"],
                    y=row["y"]
                )

                session.add(record)

            session.commit()

        finally:

            session.close()

    def clear_test_data(self):
        """
        Remove existing test data.
        """

        session = self.get_session()

        try:

            session.query(
                TestData
            ).delete()

            session.commit()

        finally:

            session.close()