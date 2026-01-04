import os

import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    """Add command-line option for browser selection."""
    parser.addoption(
        "--browserName",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to use for tests: chrome or firefox"
    )

@pytest.fixture()
def user_credentials(request):
    return request.param




@pytest.fixture(scope="function")
def setup_browser(playwright: Playwright, request):
    """Fixture to set up browser, context, and page based on command-line browser selection."""
    browser_name = request.config.getoption("--browserName")

    # Launch the appropriate browser
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    context = browser.new_context()
    page = context.new_page()
    
    # Start tracing if enabled
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Yield page for use in tests
    yield page

    # Stop tracing and save to test-results folder
    # Create test-results directory if it doesn't exist
    os.makedirs("test-results", exist_ok=True)

    # Generate unique trace file name using test name and worker ID (for parallel execution)
    test_name = request.node.name.replace("[", "_").replace("]", "_").replace("::", "_")
    worker_id = os.environ.get('PYTEST_XDIST_WORKER', 'gw0')
    trace_file = f"test-results/{test_name}_{worker_id}-trace.zip"

    try:
        context.tracing.stop(path=trace_file)
    except Exception as e:
        print(f"Warning: Failed to save trace: {e}")

    context.close()
    browser.close()

