import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#обработчик считывающий параметр из строки в powershell
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                    help="Choose language: ru, en, fr, es, etc.")

@pytest.fixture
def browser(request):
    language = request.config.getoption("language") #запарашиваем language из обработчика
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    
