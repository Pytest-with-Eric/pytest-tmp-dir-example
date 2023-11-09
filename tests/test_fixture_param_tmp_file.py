import pytest
import os


# Function to be tested
def multiply(a, b):
    return a * b


# Define a fixture for creating a temporary directory
@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path


# Define a parameterized test that takes different input values
@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (4, 5, 20), (0, 7, 0)])
def test_multiply(temp_dir, a, b, expected):
    result = multiply(a, b)

    # Create a temporary file to store the result
    result_file = temp_dir / f"result_{a}_{b}.txt"

    with open(result_file, "w") as f:
        f.write(str(result))

    assert result == expected


# Clean up: Remove the temporary files after the tests
@pytest.fixture(autouse=True)
def cleanup_temp_files(temp_dir):
    yield
    for file in temp_dir.iterdir():
        if file.is_file():
            os.remove(file)


# This will run three parameterized tests, storing results in temporary files
