"""
Custom exception hierarchy for the Ideal Function Project.
"""


class ApplicationError(Exception):
    """Base exception for all application specific errors."""
    pass


class CSVLoadError(ApplicationError):
    """Raised when CSV loading or validation fails."""
    pass


class DatabaseError(ApplicationError):
    """Raised when database operations fail."""
    pass


class FunctionSelectionError(ApplicationError):
    """Raised when ideal function selection fails."""
    pass


class MappingError(ApplicationError):
    """Raised when test point mapping fails."""
    pass


class VisualizationError(ApplicationError):
    """Raised when visualization generation fails."""
    pass