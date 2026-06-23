from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource


class PlotManager:

    @staticmethod
    def plot_training_vs_ideal(
        train_df,
        ideal_df,
        train_column,
        ideal_column,
        output_html
    ):
        """
        Plot training function
        against selected ideal function.
        """

        p = figure(
            title=f"{train_column} vs {ideal_column}",
            x_axis_label="x",
            y_axis_label="y",
            width=1000,
            height=600
        )

        p.line(
            train_df["x"],
            train_df[train_column],
            legend_label=train_column,
            line_width=3,
            color="blue"
        )

        p.line(
            ideal_df["x"],
            ideal_df[ideal_column],
            legend_label=ideal_column,
            line_width=2,
            color="red"
        )

        output_file(output_html)

        save(p)

    @staticmethod
    def plot_mapped_points(
        ideal_df,
        mapping_results,
        output_html
    ):
        """
        Plot accepted test points and
        their assigned ideal functions.
        """

        from bokeh.plotting import (
            figure,
            output_file,
            save
        )

        p = figure(
            title="Accepted Test Points by Ideal Function",
            x_axis_label="x",
            y_axis_label="y",
            width=1000,
            height=600
        )

        colors = {
            "y13": "red",
            "y24": "green",
            "y36": "orange",
            "y40": "purple"
        }

        # Plot ideal functions
        for ideal_function, color in colors.items():

            p.line(
                ideal_df["x"],
                ideal_df[ideal_function],
                legend_label=ideal_function,
                line_width=3,
                color=color
            )

        # Plot points grouped by ideal function
        for ideal_function, color in colors.items():

            points = [
                row for row in mapping_results
                if row["ideal_function"]
                == ideal_function
            ]

            if points:

                p.scatter(
                    [pnt["x"] for pnt in points],
                    [pnt["y"] for pnt in points],
                    size=10,
                    color=color,
                    marker="circle",
                    legend_label=f"{ideal_function} points"
                )

        p.legend.location = "top_right"

        output_file(output_html)

        save(p)

    @staticmethod
    def plot_distribution(
        distribution,
        output_html
    ):
        """
        Plot accepted point distribution.
        """

        functions = list(distribution.keys())
        counts = list(distribution.values())

        p = figure(
            title="Distribution of Accepted Test Points",
            x_range=functions,
            width=900,
            height=600,
            x_axis_label="Ideal Function",
            y_axis_label="Accepted Points"
        )

        p.vbar(
            x=functions,
            top=counts,
            width=0.5
        )

        output_file(output_html)

        save(p)