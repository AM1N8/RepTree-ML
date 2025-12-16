# REPTree

A Python implementation of decision trees with Reduced Error Pruning (REP) for classification and regression tasks.

## Features

- Decision tree classifier and regressor with multiple split criteria
- Reduced Error Pruning (REP) for improved generalization
- Comprehensive data preprocessing pipeline
- Feature importance calculation
- Model visualization tools
- Command-line interface for training and evaluation
- Scikit-learn compatible API

## Installation

```bash
pip install reptree
```

For visualization support:

```bash
pip install reptree[viz]
```

For CLI support:

```bash
pip install reptree[cli]
```

Install all optional dependencies:

```bash
pip install reptree[all]
```

## Quick Start

### Classification

```python
from reptree import REPTreeClassifier
from reptree.utils import train_test_split

# Load your data
X, y = load_data()

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train classifier
clf = REPTreeClassifier(
    criterion='gini',
    max_depth=10,
    pruning='rep',
    random_state=42
)
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)
accuracy = clf.score(X_test, y_test)
```

### Regression

```python
from reptree import REPTreeRegressor

# Create and train regressor
reg = REPTreeRegressor(
    criterion='variance',
    max_depth=10,
    pruning='rep',
    random_state=42
)
reg.fit(X_train, y_train)

# Make predictions
predictions = reg.predict(X_test)
r2_score = reg.score(X_test, y_test)
```

### With Preprocessing Pipeline

```python
from reptree import REPTreeClassifier, REPTreePipeline
from reptree.preprocessing import DataPreprocessor

# Create preprocessing pipeline
preprocessor = DataPreprocessor(
    handle_missing='median',
    categorical_encoding='label',
    drop_invariant=True
)

# Create full pipeline
clf = REPTreeClassifier(pruning='rep')
pipeline = REPTreePipeline(
    estimator=clf,
    preprocessor=preprocessor,
    validation_size=0.2
)

# Fit pipeline
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

## Command-Line Interface

Train a model:

```bash
reptree train data.csv --target Species --task classification --pruning rep --output model.pkl
```

Evaluate a model:

```bash
reptree evaluate model.pkl test_data.csv --target Species
```

Generate visualizations:

```bash
reptree visualize model.pkl --output-dir plots/
```

## Parameters

### REPTreeClassifier / REPTreeRegressor

- `criterion`: Split quality measure ('gini', 'entropy' for classification; 'variance', 'mae' for regression)
- `max_depth`: Maximum tree depth (None for unlimited)
- `min_samples_split`: Minimum samples required to split a node (default: 2)
- `min_samples_leaf`: Minimum samples required in a leaf (default: 1)
- `min_impurity_decrease`: Minimum impurity decrease to split (default: 0.0)
- `max_features`: Number of features to consider for splits (int, float, 'sqrt', 'log2', or None)
- `max_leaf_nodes`: Maximum number of leaf nodes (None for unlimited)
- `pruning`: Pruning strategy ('rep' or None)
- `random_state`: Random seed for reproducibility

## Visualization

```python
from reptree.visualization import TreeVisualizer

# Visualize tree structure
viz = TreeVisualizer()
viz.plot_tree(clf, feature_names=feature_names)
viz.save_figure('tree.png')

# Plot feature importance
viz.plot_feature_importance(clf, feature_names=feature_names)
viz.save_figure('importance.png')
```

## Model Persistence

```python
# Save model
clf.save('model.pkl')

# Load model
clf = REPTreeClassifier.load('model.pkl')
```

## Requirements

- Python 3.7+
- NumPy
- Optional: matplotlib, seaborn (for visualization)
- Optional: pandas, typer, loguru, rich (for CLI)

## License

MIT License

## Contributing

Contributions are welcome. Please submit pull requests or open issues on GitHub.

## Citation

If you use this implementation in your research, please cite:

```
@software{reptree,
  title = {REPTree: Decision Trees with Reduced Error Pruning},
  author = {Your Name},
  year = {2025},
  url = {https://github.com/yourusername/reptree}
}
```

## References

- Quinlan, J. R. (1987). Simplifying decision trees. International Journal of Man-Machine Studies, 27(3), 221-234.
- Breiman, L., Friedman, J., Stone, C. J., & Olshen, R. A. (1984). Classification and Regression Trees. CRC press.

