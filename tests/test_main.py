from code_coverage.main import main


def test_main(capsys) -> None:
    # Arrange
    expected = "Hello, world!\n"
    main()
    captured = capsys.readouterr()
    # Act

    # Assert
    assert captured.out == expected
