# Ideal Function Selection and Test Point Mapping Using Python

## Overview

This project was developed as part of the Programming with Python module at IU International University of Applied Sciences.

The objective of the project was to identify the most suitable ideal functions from a collection of candidate functions provided and then assign test data points to the selected functions using mathematically defined acceptance criteria.

## Project Objectives

* Load and process training dataset, ideal dataset and test dataset.
* Select the most suitable ideal functions using Sum of Squared Errors (SSE).
* Calculate acceptance thresholds based on maximum deviations.
* Map test data points to the selected ideal functions.
* Store datasets and results in a SQLite database.
* Generate graphical visualizations of the analytical results.
* Use automated testing to verify the functions.

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* Bokeh
* Pytest

## Project Structure

core/ - Function selection and mapping logic

database/ - Database models and management

visualization/ - Graph generation

tests/ - Automated tests

data/ - Input datasets

main.py - Application entry point

## Running the Application

python main.py

## Running Tests

pytest

## Graph Outputs Generated

* Training vs Ideal Function Comparisons
* Accepted Test Point Mapping Visualization
* Distribution of Accepted Test Points
* SQLite Database Storage

## Author

Gabriel Mashenene

Master of Computer Science

IU International University of Applied Sciences
