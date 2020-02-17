import pytest

from selenium import webdriver
from pathlib import Path


@pytest.fixture()
def project_root():
    return Path.cwd()


@pytest.fixture()
def chromedriver_path(project_root):
    return project_root / "chromedriver.exe"


@pytest.fixture()
def browser(chromedriver_path):
    driver = webdriver.Chrome(executable_path=str(chromedriver_path))

    yield driver

    driver.close()
