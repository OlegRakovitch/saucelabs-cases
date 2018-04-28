import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

_SCRIPT_LOCATION = (
    "https://raw.githubusercontent.com/OlegRakovitch/saucelabs-cases"
    "/master/edge_open_window_returns_null/allow_popups.cmd"
)
_PAGE_LOCATION = (
    "https://s3.amazonaws.com/saucelabs-cases"
    "/edge_open_window_returns_null/s3_file.html"
)
_SAUCELABS_SERVER = (
    "http://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}"
    "@ondemand.saucelabs.com:80/wd/hub"
)

def check_env():
    assert "SAUCE_USERNAME" in os.environ
    assert "SAUCE_ACCESS_KEY" in os.environ


def get_body(driver):
    script = "return document.body && document.body.innerHTML;"
    return driver.execute_script(script)


def run_example():
    check_env()

    options = webdriver.DesiredCapabilities.EDGE
    options["screenResolution"] = "1920x1080"
    options["platform"] = "Windows 10"
    options["idleTimeout"] = 1200
    options["prerun"] = {
        "executable": _SCRIPT_LOCATION,
        "background": "false"
    }
    server_url = _SAUCELABS_SERVER.format(**os.environ)

    try:
        driver = webdriver.Remote(server_url, options)
        driver.get(_PAGE_LOCATION)
        body = webdriver.support.ui.WebDriverWait(driver, 30).until(get_body)
        print("Result: {}".format(body))
    finally:
        driver.quit()

if __name__ == "__main__":

    run_example()
