import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name not in ["chrome", "firefox"]:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\nstart chrome browser for test with language {user_language}..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        print(f"\nstart firefox browser for test with language {user_language}..")
        browser = webdriver.Firefox(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()