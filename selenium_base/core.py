# anyisalin@gmail.com 2017-06-25
import selenium
from selenium import webdriver


def get_driver(browser='PhantomJS', *args, **kwargs):
    driver_class = getattr(webdriver, browser)
    if driver_class.__bases__ != (selenium.webdriver.remote.webdriver.WebDriver,):
        raise AttributeError('Must WebDriver subclasses')
    return driver_class(*args, **kwargs)

