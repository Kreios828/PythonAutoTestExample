import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') #headless если не нужен UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1366,768')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='drivers/97.0.4692.71', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.decathlon.com/'
    if request.cls is not None: # Проверка, что тесты в классе
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()

# Костыль для России - закрытие окна приветствия
    driver.find_element(By.XPATH, '//*[@id="gateway"]/button').click()

    yield driver
    driver.quit()
