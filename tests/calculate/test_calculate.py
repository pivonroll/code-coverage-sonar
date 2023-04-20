from code_coverage.calculator.calculate import calculate


def test_calculate() -> None:
    # Arrange
    expected = 8
    # Act
    actual = calculate(4)
    # Assert
    assert actual == expected
