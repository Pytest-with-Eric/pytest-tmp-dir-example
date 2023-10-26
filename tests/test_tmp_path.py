import pytest


def test_create_and_check_file(tmp_path):
    # Use tmp_path to create a temporary directory
    temp_dir = tmp_path / "my_temp_dir"
    temp_dir.mkdir()

    # Create a file inside the temporary directory
    temp_file = temp_dir / "test_file.txt"
    temp_file.write_text("Hello, pytest!")

    # Check if the file exists
    assert temp_file.is_file()

    # Read the file's contents
    assert temp_file.read_text() == "Hello, pytest!"
