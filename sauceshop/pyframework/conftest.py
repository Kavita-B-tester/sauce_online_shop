import os

import pytest
from selenium import webdriver
driver=None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="browser selection"
    )
@pytest.fixture(scope="function")
def BrowserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def runtest_report(item):
    pytest_html=item.config.pluginmanager.getpluginsmanager().getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra=getattr(report, "extra", [])
    if report.when=="call" or report.when=="setup":
        xfail=getattr(report,"waxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir=os.path.join(os.path.dirname(__file__), "testreports")
            file_name=os.path.join(reports_dir,report.nodeid.replace("::","_") + "png")
            print("filename is",file_name)
            _captchure_screenshot(file_name)
            if file_name:
                html='<div><img src="%s" alt="screenshot" style="width:30px;height:220px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra=extra


def _captchure_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
