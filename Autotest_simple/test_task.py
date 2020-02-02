import time
from selenium import webdriver
import pytest

# Fixture for Chrome
@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    print("Browser closed")

@pytest.mark.usefixtures("driver_init")
class Test_businesschain():
    #ТС 12 Авторизация зарегистрированного пользователя
    def test_TC_12(self):
        driver = self.driver
        driver.get("https://trunk.businesschain.io/registrateUser")
        driver.find_element_by_css_selector("span.visible-desktop").click()
        driver.find_element_by_css_selector("#username").click()
        driver.find_element_by_css_selector("#username").clear()
        driver.find_element_by_css_selector("#username").send_keys("kubartphil@gmail.com")
        driver.find_element_by_css_selector("#password").click()
        driver.find_element_by_css_selector("#password").click()
        driver.find_element_by_css_selector("#password").clear()
        driver.find_element_by_css_selector("#password").send_keys("1234abcd")
        driver.find_element_by_css_selector("button.btn.btn-primary.btn-block-mobile").click()
        time.sleep(5)
    #ТС 00 Выход из аккаунта пользователя
    def test_TC_00(self):
        driver = self.driver
        driver.get("https://trunk.businesschain.io/registrateUser")
        driver.find_element_by_css_selector("button.btn.btn-clear.dropdown-toggle.visible-desktop").click()
        driver.find_element_by_xpath("//div[4]/div/ul/li[2]/a").click()
        time.sleep(5)

