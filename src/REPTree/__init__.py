"""
REPTree: Reduced Error Pruning Tree Implementation

A scikit-learn compatible decision tree implementation with Reduced Error Pruning.
"""

from ._version import __version__
from .tree import REPTreeClassifier, REPTreeRegressor
from .preprocessing import DataPreprocessor, DataValidator
from .pipeline import REPTreePipeline

__all__ = [
    '__version__',
    'REPTreeClassifier',
    'REPTreeRegressor',
    'DataPreprocessor',
    'DataValidator',
    'REPTreePipeline',
]