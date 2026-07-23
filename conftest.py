import pytest

pytest_plugins = (
    "fixtures.browsers",
    "fixtures.pages"
)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": True
    }
