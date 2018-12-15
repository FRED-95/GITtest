from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost/index.php")
    return driver
