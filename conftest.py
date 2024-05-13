

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from faker import Faker


@pytest.fixture(autouse=True)
def browser():

    s = Service(executable_path='C:/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    yield driver
    driver.quit()