from collections import Counter

from core.csv_loader import CSVLoader
from core.selector import FunctionSelectionService
from core.mapper import MappingService

from database.db_manager import DatabaseManager

from visualization.plot_manager import PlotManager


def main():

    print("=" * 60)
    print("IDEAL FUNCTION PROJECT")
    print("=" * 60)

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    db = DatabaseManager()
 
    db.create_database()

    print("\nDatabase initialized.")

    # --------------------------------------------------
    # Load datasets
    # --------------------------------------------------

    train_df = CSVLoader.load_csv(
        "data/train.csv"
    )

    ideal_df = CSVLoader.load_csv(
        "data/ideal.csv"
    )

    test_df = CSVLoader.load_csv(
        "data/test.csv"
    )

    print("\nDatasets loaded.")

    # --------------------------------------------------
    # Function Selection
    # --------------------------------------------------

    selector = FunctionSelectionService()

    selected_functions = selector.select_all_functions(
        train_df,
        ideal_df
    )

    print("\nSelected Ideal Functions:")

    for train_col, result in selected_functions.items():

        print(
            f"{train_col} -> "
            f"{result['ideal_function']}"
        )

    # --------------------------------------------------
    # Threshold Calculation
    # --------------------------------------------------

    mapper = MappingService()

    thresholds = {}

    for train_col, result in selected_functions.items():

        ideal_col = result["ideal_function"]

        max_dev = mapper.calculate_max_deviation(
            train_df[train_col],
            ideal_df[ideal_col]
        )

        threshold = mapper.calculate_threshold(
            max_dev
        )

        thresholds[ideal_col] = threshold

    print("\nThresholds:")

    for func, value in thresholds.items():

        print(
            f"{func}: {value:.6f}"
        )

    # --------------------------------------------------
    # Map Test Points
    # --------------------------------------------------

    mapping_results = mapper.map_all_points(
        test_df,
        ideal_df,
        thresholds
    )

    print("\nMapping completed.")

    print(
        f"Accepted: {len(mapping_results)}"
    )

    print(
        f"Rejected: "
        f"{len(test_df) - len(mapping_results)}"
    )

    # --------------------------------------------------
    # Distribution
    # --------------------------------------------------

    distribution = Counter(
        row["ideal_function"]
        for row in mapping_results
    )

    PlotManager.plot_distribution(
    distribution,
    "plots/mapping_distribution.html"
    )

    print("\nDistribution:")

    for func, count in distribution.items():

        print(
            f"{func}: {count}"
        )

    # --------------------------------------------------
    # Save Results
    # --------------------------------------------------
    db.clear_training_data()
    db.save_training_data(train_df)

    db.clear_ideal_functions()
    db.save_ideal_data(ideal_df)

    db.clear_test_data()
    db.save_test_data(test_df)

    db.clear_mapping_results()

    db.save_mapping_results(
        mapping_results
    )

    print(
        "\nMapping results saved."
    )

    # --------------------------------------------------
    # Generate Plots
    # --------------------------------------------------

    selected_pairs = {
        "y1": "y13",
        "y2": "y24",
        "y3": "y36",
        "y4": "y40"
    }

    for train_col, ideal_col in selected_pairs.items():

        PlotManager.plot_training_vs_ideal(
            train_df,
            ideal_df,
            train_col,
            ideal_col,
            f"plots/{train_col}_vs_{ideal_col}.html"
        )

    PlotManager.plot_mapped_points(
        ideal_df,
        mapping_results,
        "plots/mapped_points_colored.html"
    )

    print(
    "\nGenerated Figures:"
    )

    print("1. y1_vs_y13.html")
    print("2. y2_vs_y24.html")
    print("3. y3_vs_y36.html")
    print("4. y4_vs_y40.html")
    print("5. mapped_points_colored.html")
    print("6. mapping_distribution.html")

    print("\nProject completed successfully.")


if __name__ == "__main__":
    main()

    