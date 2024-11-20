import pytest


@pytest.fixture
def input_value():
    input = 39
    return input


def pytest_configure(config):
    # register your new marker to avoid warnings
    config.addinivalue_line(
        "markers",
        "key: smoke"
    )
