import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
import geckodriver_autoinstaller


# @pytest.fixture()
# def setup():
#     chromedriver_autoinstaller.install()
#     driver = webdriver.Chrome(service=Service())
#     print("Launching chrome browser.........")
#     return driver
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(service=Service())
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        geckodriver_autoinstaller.install()
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'denefits'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'guri'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
