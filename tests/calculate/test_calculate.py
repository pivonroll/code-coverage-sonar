from code_coverage.calculator.calculate import calculate, square


def test_calculate() -> None:
    # Arrange
    expected = 8
    # Act
    actual = calculate(4)
    # Assert
    assert actual == expected


def test_square() -> None:
    # Arrange
    expected = 16
    # Act
    actual = square(4)
    # Assert
    assert actual == expected
