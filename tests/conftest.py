import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Declaring command line argruments

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Main\\Python\\PySeFramework\\tests\\chromedriver.exe")
    elif browser_name == "firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path="C:\\Main\\Python\\PySeFramework\\tests\\geckodriver.exe",options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\Main\\Python\\PySeFramework\\tests\\msedgedriver.exe")

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


