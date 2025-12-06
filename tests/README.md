# Test Suite for RepTree-ML

## Overview

This directory contains comprehensive tests for the RepTree-ML library. The tests are organized by module and cover unit tests, integration tests, and edge cases.

## Test Organization

```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Pytest configuration and shared fixtures
├── test_tree.py             # Tests for REPTreeClassifier and REPTreeRegressor
├── test_node.py             # Tests for TreeNode data structure
├── test_metrics.py          # Tests for impurity and evaluation metrics
├── test_splitter.py         # Tests for split finding algorithms
├── test_pruning.py          # Tests for Reduced Error Pruning
└── test_utils.py            # Tests for utility functions
```

## Running Tests

### Run all tests
```bash
pytest tests/
```

### Run specific test file
```bash
pytest tests/test_tree.py
```

### Run specific test class
```bash
pytest tests/test_tree.py::TestREPTreeClassifier
```

### Run specific test function
```bash
pytest tests/test_tree.py::TestREPTreeClassifier::test_fit_iris_dataset
```

### Run with verbose output
```bash
pytest tests/ -v
```

### Run with coverage report
```bash
pytest tests/ --cov=reptree --cov-report=html
```

### Run only fast tests (skip slow tests)
```bash
pytest tests/ -m "not slow"
```

## Test Coverage

### test_tree.py
- **REPTreeClassifier**: 30+ tests
  - Initialization and parameter validation
  - Fitting on various datasets (binary, multiclass)
  - Prediction and probability estimation
  - Feature importance calculation
  - Pruning functionality
  - Model persistence (save/load)
  - Edge cases (single class, missing values, etc.)

- **REPTreeRegressor**: 20+ tests
  - Initialization and parameter validation
  - Fitting on regression datasets
  - Prediction accuracy
  - Different criteria (variance, MAE)
  - Pruning functionality
  - Model persistence

### test_node.py
- Node creation and properties
- Tree traversal methods (depth, node counting)
- Prediction methods (single sample and batch)
- Parent-child relationships
- Handling missing values
- Node conversion (to leaf)
- Memory efficiency (__slots__)

### test_metrics.py
- **Impurity Metrics**: Gini, entropy, variance, MAE
- **Information Gain**: Various criteria and edge cases
- **Classification Metrics**: Accuracy, confusion matrix
- **Regression Metrics**: MSE, MAE, R²
- Edge cases: Empty arrays, perfect predictions, extreme values

### test_splitter.py
- Split finding algorithms
- Threshold selection strategies
- Feature subsampling
- Constraint enforcement (min_samples_split, min_samples_leaf)
- Handling missing values
- Binary and continuous features
- Regression and classification splits

### test_pruning.py
- REP algorithm correctness
- Pruning on various tree structures
- Classification and regression pruning
- Performance improvement validation
- Sample routing through tree
- Error computation
- Edge cases (empty validation set, single node)

### test_utils.py
- Array validation (check_array, check_X_y, check_is_fitted)
- Train-test split functionality
- Feature importance calculation
- Tree export functions (text, dictionary)
- Tree statistics
- Edge cases (empty arrays, single samples)

## Test Fixtures

The `conftest.py` file provides shared fixtures:

- `simple_classification_data`: Small binary classification dataset
- `simple_regression_data`: Small regression dataset
- `iris_dataset`: Classic iris dataset
- `multiclass_data`: Generated multiclass dataset
- `regression_data`: Generated regression dataset
- `data_with_nan`: Dataset with missing values
- `tiny_tree_data`: Minimal dataset for tree construction

## Writing New Tests

### Test Naming Convention
- Test files: `test_<module>.py`
- Test classes: `Test<ClassName>`
- Test functions: `test_<description>`

### Example Test
```python
def test_feature_description(fixture_name):
    """
    Brief description of what is being tested.
    """
    # Arrange
    X, y = fixture_name
    clf = REPTreeClassifier()
    
    # Act
    clf.fit(X, y)
    predictions = clf.predict(X)
    
    # Assert
    assert predictions.shape == y.shape
```

### Using Fixtures
```python
def test_with_iris_data(iris_dataset):
    """Test using the iris dataset fixture"""
    X, y = iris_dataset
    # ... test code ...
```

### Testing Exceptions
```python
def test_invalid_parameter():
    """Test that invalid parameter raises error"""
    with pytest.raises(ValueError, match="expected error message"):
        REPTreeClassifier(invalid_param=123)
```

## Dependencies

Required packages for running tests:
- pytest >= 6.0
- numpy
- scikit-learn (for dataset generation and comparison)

Optional packages:
- pytest-cov (for coverage reports)
- pytest-xdist (for parallel test execution)

Install test dependencies:
```bash
pip install pytest pytest-cov pytest-xdist
```

## Continuous Integration

These tests are designed to be run in CI/CD pipelines. Example GitHub Actions workflow:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        pip install -e .
        pip install pytest pytest-cov
    - name: Run tests
      run: pytest tests/ --cov=reptree
```

## Test Statistics

- **Total Test Files**: 7
- **Estimated Total Tests**: 150+
- **Average Test Execution Time**: < 30 seconds
- **Test Coverage Goal**: > 90%

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure reptree package is installed: `pip install -e .`
   - Check Python path includes project root

2. **Fixture Not Found**
   - Verify `conftest.py` is in the tests directory
   - Check fixture name spelling

3. **Random Failures**
   - Ensure `random_state` is set in tests
   - Check for race conditions in parallel tests

## Contributing

When adding new features to RepTree-ML:
1. Write tests first (TDD approach recommended)
2. Ensure all tests pass before submitting PR
3. Aim for > 90% code coverage for new code
4. Add docstrings to test functions
5. Update this README if adding new test files

## Contact

For questions about tests or to report issues:
- Open an issue on GitHub
- Contact the development team

---

**Last Updated**: November 2025
