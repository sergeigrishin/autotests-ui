import pytest

SYSTEM_VERSION = "v3.3.0"

@pytest.mark.skip(reason="Пропустить какой-то тест")
def test_feature_in_development():
    ...


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0"
)
def test_system_version_valid():
    ...


@pytest.mark.xfail #Был найден баг, функционал не работает из-за бага
def test_system_version_invalid():
    ...