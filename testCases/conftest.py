import pytest
import undetected_chromedriver as uc
from selenium import webdriver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get("setup")  # or whatever your driver fixture is named
        if driver:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to report
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(screenshot_path))

# Function to add custom command-line arguments
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for test")


# Fixture to fetch the browser name from the command line
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Fixture to initialize the browser
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        print("Launching Chrome browser")
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        driver = uc.Chrome(options=options, headless=False)
    elif browser == "edge":
        print("Launching Edge browser")
        driver = webdriver.Edge()
    else:
        raise Exception(f"Browser '{browser}' is not supported.")

    yield driver
    print("Closing browser")
    driver.quit()