import pytest
from utilities.color_print import print_yel
from base.webdriver_factory import WebdriverFactory
@pytest.yield_fixture()

def setUp():
    print ("\nRunning  method level setUp")
    yield
    print("\nOnce yield method level TEARDOWN after every method")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request,browser,os_type):
    print_yel("\nRunning onetimesetUp test")
    wdf = WebdriverFactory(browser)
    driver = wdf.get_driver_instance()
    driver_name = str(driver).split(".")
    print_yel("Running on <<{}>> browser".format(driver_name[2]))
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print_yel("\nOnce yield after all tests are done")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type",help='operating system')

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="module")
def os_type(request):
    return request.config.getoption("--os_type")